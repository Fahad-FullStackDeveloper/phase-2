from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid


class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    recurrence_pattern: Optional[str] = None  # daily, weekly, monthly, yearly
    recurrence_end_date: Optional[datetime] = None
    reminder_time: Optional[datetime] = None


class Task(TaskBase, table=True):
    """
    Represents a user's task with title, description, completion status, creation date, and update timestamp
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column_kwargs={"primary_key": True})
    user_id: uuid.UUID
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)