from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Optional
from datetime import timedelta
from src.database import get_session
from src.models.user import User, UserBase
from src.services.auth_service import AuthService
from src.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user_data: UserBase, password: str, session: Session = Depends(get_session)):
    """Register a new user"""
    auth_service = AuthService(session)
    user_service = UserService(session)
    
    # Check if user already exists
    existing_user = user_service.get_user_by_email(user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    
    # Create new user
    user = user_service.create_user(user_data, password)
    
    # Create session
    auth_service.create_session(user.id)
    
    return {
        "success": True,
        "message": "User registered successfully",
        "user": user
    }


@router.post("/login")
def login(email: str, password: str, session: Session = Depends(get_session)):
    """Login a user"""
    auth_service = AuthService(session)
    
    user = auth_service.authenticate_user(email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=30)
    access_token = auth_service.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    # Create session
    auth_service.create_session(user.id)
    
    return {
        "success": True,
        "message": "Login successful",
        "token": access_token,
        "user": user
    }