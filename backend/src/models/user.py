from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid


class UserBase(SQLModel):
    email: str
    name: str


class User(UserBase, table=True):
    """
    Represents an authenticated user with email, name, and account creation date
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column_kwargs={"primary_key": True})
    email: str = Field(sa_column_kwargs={"unique": True, "index": True})
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Session(SQLModel, table=True):
    """
    Represents an authenticated user session with JWT token validity
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column_kwargs={"primary_key": True})
    user_id: uuid.UUID
    token: str
    expires_at: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)