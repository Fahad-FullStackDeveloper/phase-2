// backend/src/services/recurring_task_service.py
from sqlmodel import Session, select
from datetime import datetime, timedelta
from typing import List
import uuid
from ..models.task import Task


class RecurringTaskService:
    def __init__(self, session: Session):
        self.session = session

    def generate_recurring_tasks(self):
        """Generate new task instances based on recurrence patterns"""
        # Get all recurring tasks that should generate new instances
        statement = select(Task).where(
            Task.recurrence_pattern.is_not(None),
            Task.recurrence_end_date >= datetime.utcnow()
        )
        recurring_tasks = self.session.exec(statement).all()

        new_tasks = []
        for task in recurring_tasks:
            # Check if a new instance should be created based on the recurrence pattern
            should_create_new = self._should_create_new_instance(task)
            if should_create_new:
                new_task = self._create_new_task_instance(task)
                new_tasks.append(new_task)

        return new_tasks

    def _should_create_new_instance(self, task: Task) -> bool:
        """Determine if a new task instance should be created based on recurrence pattern"""
        now = datetime.utcnow()
        
        # Get the most recent instance of this recurring task
        statement = select(Task).where(
            Task.title == task.title,
            Task.description == task.description,
            Task.created_at >= now - timedelta(days=365)  # Look back 1 year
        ).order_by(Task.created_at.desc()).limit(1)
        
        last_instance = self.session.exec(statement).first()
        
        if not last_instance:
            # If no instance exists, create one
            return True
            
        # Check if enough time has passed based on the recurrence pattern
        if task.recurrence_pattern == 'daily':
            return (now - last_instance.created_at).days >= 1
        elif task.recurrence_pattern == 'weekly':
            return (now - last_instance.created_at).days >= 7
        elif task.recurrence_pattern == 'monthly':
            return (now - last_instance.created_at).days >= 30
        elif task.recurrence_pattern == 'yearly':
            return (now - last_instance.created_at).days >= 365
        
        return False

    def _create_new_task_instance(self, original_task: Task) -> Task:
        """Create a new instance of a recurring task"""
        new_task = Task(
            title=original_task.title,
            description=original_task.description,
            completed=False,  # New instances start as incomplete
            user_id=original_task.user_id,
            recurrence_pattern=original_task.recurrence_pattern,
            recurrence_end_date=original_task.recurrence_end_date,
            reminder_time=original_task.reminder_time
        )
        
        self.session.add(new_task)
        self.session.commit()
        self.session.refresh(new_task)
        
        return new_task

    def schedule_recurring_tasks(self):
        """Method to be called periodically to generate recurring tasks"""
        return self.generate_recurring_tasks()