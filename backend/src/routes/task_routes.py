from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Optional
from uuid import UUID
from ..database import get_session
from ..models.task import Task, TaskBase
from ..models.user import User
from ..services.task_service import TaskService
from ..services.auth_service import AuthService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_current_user_from_token(token: str, session: Session) -> User:
    """Helper to get current user from token"""
    auth_service = AuthService(session)
    user = auth_service.get_current_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@router.get("/")
def get_tasks(
    completed: Optional[bool] = None,
    limit: int = 20,
    offset: int = 0,
    token: str = Depends(...),  # In a real app, this would be handled by a security dependency
    session: Session = Depends(get_session)
):
    """Get user's tasks"""
    # Note: In a real implementation, we'd extract user from token
    # For now, we'll simulate this with a placeholder
    current_user = get_current_user_from_token(token, session)
    
    task_service = TaskService(session)
    tasks = task_service.get_tasks_by_user(current_user.id, completed)
    
    # Apply pagination
    paginated_tasks = tasks[offset:offset + limit]
    
    return {
        "success": True,
        "tasks": paginated_tasks,
        "total": len(tasks)
    }


@router.post("/")
def create_task(
    task_data: TaskBase,
    token: str = Depends(...),  # In a real app, this would be handled by a security dependency
    session: Session = Depends(get_session)
):
    """Create a new task for the authenticated user"""
    current_user = get_current_user_from_token(token, session)
    
    task_service = TaskService(session)
    task = task_service.create_task(current_user.id, task_data)
    
    return {
        "success": True,
        "message": "Task created successfully",
        "task": task
    }


@router.get("/{task_id}")
def get_task(
    task_id: UUID,
    token: str = Depends(...),  # In a real app, this would be handled by a security dependency
    session: Session = Depends(get_session)
):
    """Get a specific task by ID for the authenticated user"""
    current_user = get_current_user_from_token(token, session)
    
    task_service = TaskService(session)
    task = task_service.get_task_by_id(task_id, current_user.id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return {
        "success": True,
        "task": task
    }


@router.put("/{task_id}")
def update_task(
    task_id: UUID,
    task_data: TaskBase,
    token: str = Depends(...),  # In a real app, this would be handled by a security dependency
    session: Session = Depends(get_session)
):
    """Update an existing task for the authenticated user"""
    current_user = get_current_user_from_token(token, session)
    
    task_service = TaskService(session)
    task = task_service.update_task(task_id, current_user.id, task_data)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return {
        "success": True,
        "message": "Task updated successfully",
        "task": task
    }


@router.delete("/{task_id}")
def delete_task(
    task_id: UUID,
    token: str = Depends(...),  # In a real app, this would be handled by a security dependency
    session: Session = Depends(get_session)
):
    """Delete a task for the authenticated user"""
    current_user = get_current_user_from_token(token, session)
    
    task_service = TaskService(session)
    success = task_service.delete_task(task_id, current_user.id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return {
        "success": True,
        "message": "Task deleted successfully"
    }


@router.patch("/{task_id}/complete")
def toggle_task_completion(
    task_id: UUID,
    token: str = Depends(...),  # In a real app, this would be handled by a security dependency
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a task"""
    current_user = get_current_user_from_token(token, session)
    
    task_service = TaskService(session)
    task = task_service.toggle_task_completion(task_id, current_user.id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return {
        "success": True,
        "message": "Task completion status updated",
        "task": task
    }