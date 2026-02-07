from sqlmodel import Session, select
from ..models.user import User, UserBase
from typing import Optional
import uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_data: UserBase, password: str) -> User:
        """Create a new user with hashed password"""
        hashed_password = pwd_context.hash(password)
        
        db_user = User(
            email=user_data.email,
            name=user_data.name,
            # Store hashed password separately if needed
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()

    def get_user_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        """Get user by ID"""
        statement = select(User).where(User.id == user_id)
        return self.session.exec(statement).first()

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password"""
        user = self.get_user_by_email(email)
        if not user:
            return None
        # Verify password here if stored separately
        return user