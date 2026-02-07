# Data Model: Full-Stack Todo Web Application

## Entity: User
**Description**: Represents an authenticated user with email, name, and account creation date

**Fields**:
- id (UUID, Primary Key, Auto-generated)
- email (String, 1-255 characters, Unique, Required)
- name (String, 1-100 characters, Required)
- created_at (DateTime, Auto-generated)
- updated_at (DateTime, Auto-generated)

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Name must be 1-100 characters
- Created_at and updated_at are automatically managed by the system

**Relationships**:
- One-to-Many: User has many Tasks

## Entity: Task
**Description**: Represents a user's task with title, description, completion status, creation date, and update timestamp

**Fields**:
- id (UUID, Primary Key, Auto-generated)
- user_id (UUID, Foreign Key to User.id, Required)
- title (String, 1-100 characters, Required)
- description (String, 0-1000 characters, Optional)
- completed (Boolean, Default: false)
- created_at (DateTime, Auto-generated)
- updated_at (DateTime, Auto-generated)
- recurrence_pattern (String, 0-50 characters, Optional)
- recurrence_end_date (DateTime, Optional)
- reminder_time (DateTime, Optional)

**Validation Rules**:
- Title must be 1-100 characters
- Description must be 0-1000 characters if provided
- User_id must reference an existing user
- Completed defaults to false
- Recurrence_pattern values: 'daily', 'weekly', 'monthly', 'yearly'
- If recurrence_pattern is set, recurrence_end_date may be specified

**State Transitions**:
- Status changes from incomplete to complete when marked as done
- Status changes from complete to incomplete when unmarked

**Relationships**:
- Many-to-One: Task belongs to one User

## Entity: Session
**Description**: Represents an authenticated user session with JWT token validity

**Fields**:
- id (UUID, Primary Key, Auto-generated)
- user_id (UUID, Foreign Key to User.id, Required)
- token (String, 255 characters, Required)
- expires_at (DateTime, Required)
- created_at (DateTime, Auto-generated)

**Validation Rules**:
- Token must be unique
- Expires_at must be in the future
- User_id must reference an existing user

**Relationships**:
- Many-to-One: Session belongs to one User