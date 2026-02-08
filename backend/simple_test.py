from sqlmodel import SQLModel, Field

# Simple model definition to test
class SimpleUser(SQLModel):
    email: str = Field(default=..., unique=True, index=True)
    name: str = Field(default=...)

print("SimpleUser class defined successfully!")

# Try to create an instance
user = SimpleUser(email="test@example.com", name="Test User")
print(f"User instance created: {user}")