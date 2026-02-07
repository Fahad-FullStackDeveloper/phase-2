from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime
import uuid

if TYPE_CHECKING:
    from .task import Task  # Forward reference for relationship


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, max_length=255)
    name: str = Field(max_length=100)


class User(UserBase, table=True):
    """
    Represents an authenticated user with email, name, and account creation date
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to tasks
    tasks: list["Task"] = Relationship(back_populates="user")


class Session(SQLModel, table=True):
    """
    Represents an authenticated user session with JWT token validity
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    token: str = Field(max_length=255, unique=True)
    expires_at: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)