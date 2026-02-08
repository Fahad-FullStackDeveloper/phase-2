#!/usr/bin/env python
# Test script to check if models can be imported correctly

try:
    print("Attempting to import SQLModel components...")
    from sqlmodel import SQLModel, Field
    
    print("Defining a simple test model...")
    class TestUserBase(SQLModel):
        email: str = Field(unique=True, index=True, max_length=255)
        name: str = Field(max_length=100)
    
    print("TestUserBase defined successfully!")
    
    print("Attempting to import the actual models...")
    from src.models.user import UserBase, User
    print("Models imported successfully!")
    
    print("Creating a test instance...")
    test_user = UserBase(email="test@example.com", name="Test User")
    print(f"Test user created: {test_user}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()