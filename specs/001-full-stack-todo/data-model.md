# Data Model: Full-Stack Todo Web Application

## Entities

### User
Represents an authenticated user with email, name, and account creation date

**Fields:**
- id: string (primary key, UUID)
- email: string (unique, required)
- name: string (required, 1-100 characters)
- created_at: datetime (timestamp)
- updated_at: datetime (timestamp)

**Validation:**
- Email must be a valid email format
- Name must be 1-100 characters
- Email must be unique across all users

### Task
Represents a user's task with title, description, completion status, creation date, and update timestamp

**Fields:**
- id: integer (primary key, auto-increment)
- user_id: string (foreign key to User.id, required)
- title: string (required, 1-100 characters)
- description: string (optional, max 1000 characters)
- completed: boolean (default false)
- created_at: datetime (timestamp)
- updated_at: datetime (timestamp)
- due_date: datetime (optional)
- recurrence_pattern: string (optional, enum: daily, weekly, monthly, yearly, none)

**Validation:**
- Title must be 1-100 characters
- Description must be 0-1000 characters if provided
- User_id must reference an existing user
- Due date must be in the future if provided

### Session
Represents an authenticated user session with JWT token validity

**Fields:**
- id: string (primary key, UUID)
- user_id: string (foreign key to User.id, required)
- token_hash: string (required, hashed JWT)
- expires_at: datetime (timestamp)
- created_at: datetime (timestamp)

**Validation:**
- User_id must reference an existing user
- Token hash must be unique
- Expires_at must be in the future

## Relationships
- User (1) : Task (Many) - A user can have many tasks
- User (1) : Session (Many) - A user can have multiple active sessions

## State Transitions
- Task: pending → completed (when marked as complete)
- Task: completed → pending (when unmarked as complete)
- Session: active → expired (when expires_at is reached)