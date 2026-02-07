from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    recurrence_pattern: Optional[str] = Field(default=None, max_length=50)  # daily, weekly, monthly, yearly
    recurrence_end_date: Optional[datetime] = Field(default=None)
    reminder_time: Optional[datetime] = Field(default=None)


class Task(TaskBase, table=True):
    """
    Represents a user's task with title, description, completion status, creation date, and update timestamp
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to user
    user: "User" = Relationship(back_populates="tasks")