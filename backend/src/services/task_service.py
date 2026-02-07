from sqlmodel import Session, select
from ..models.task import Task, TaskBase
from typing import Optional, List
import uuid
from datetime import datetime


class TaskService:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, user_id: uuid.UUID, task_data: TaskBase) -> Task:
        """Create a new task for a user"""
        db_task = Task(
            user_id=user_id,
            title=task_data.title,
            description=task_data.description,
            completed=task_data.completed,
            recurrence_pattern=task_data.recurrence_pattern,
            recurrence_end_date=task_data.recurrence_end_date,
            reminder_time=task_data.reminder_time
        )
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return db_task

    def get_tasks_by_user(self, user_id: uuid.UUID, completed: Optional[bool] = None) -> List[Task]:
        """Get all tasks for a user, optionally filtered by completion status"""
        statement = select(Task).where(Task.user_id == user_id)
        if completed is not None:
            statement = statement.where(Task.completed == completed)
        statement = statement.order_by(Task.created_at.desc())
        return self.session.exec(statement).all()

    def get_task_by_id(self, task_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Task]:
        """Get a specific task by ID for a user"""
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        return self.session.exec(statement).first()

    def update_task(self, task_id: uuid.UUID, user_id: uuid.UUID, task_data: TaskBase) -> Optional[Task]:
        """Update a task for a user"""
        db_task = self.get_task_by_id(task_id, user_id)
        if not db_task:
            return None
        
        # Update fields
        for field, value in task_data.dict(exclude_unset=True).items():
            setattr(db_task, field, value)
        
        db_task.updated_at = datetime.utcnow()
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return db_task

    def delete_task(self, task_id: uuid.UUID, user_id: uuid.UUID) -> bool:
        """Delete a task for a user"""
        db_task = self.get_task_by_id(task_id, user_id)
        if not db_task:
            return False
        
        self.session.delete(db_task)
        self.session.commit()
        return True

    def toggle_task_completion(self, task_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Task]:
        """Toggle the completion status of a task"""
        db_task = self.get_task_by_id(task_id, user_id)
        if not db_task:
            return None
        
        db_task.completed = not db_task.completed
        db_task.updated_at = datetime.utcnow()
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return db_task