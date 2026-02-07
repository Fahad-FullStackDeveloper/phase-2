# API Contracts: Full-Stack Todo Web Application

## Base URL
- Development: http://localhost:8000
- Production: https://api.todoapp.com

## Authentication
All endpoints require JWT token in header:
```
Authorization: Bearer <jwt_token>
```

## Endpoints

### User Registration and Authentication

#### POST /api/auth/register
Register a new user account.

**Request Body:**
```json
{
  "email": "string (required)",
  "password": "string (required, min 8 chars)",
  "name": "string (required, 1-100 chars)"
}
```

**Response (201 Created):**
```json
{
  "id": "string (UUID)",
  "email": "string",
  "name": "string",
  "created_at": "datetime"
}
```

**Response (400 Bad Request):**
- Invalid email format
- Password too short
- Name exceeds 100 characters
- Email already exists

#### POST /api/auth/login
Authenticate user and return JWT token.

**Request Body:**
```json
{
  "email": "string (required)",
  "password": "string (required)"
}
```

**Response (200 OK):**
```json
{
  "access_token": "string (JWT)",
  "refresh_token": "string (JWT)",
  "user": {
    "id": "string (UUID)",
    "email": "string",
    "name": "string"
  }
}
```

**Response (401 Unauthorized):**
- Invalid credentials

### Task Management

#### GET /api/{user_id}/tasks
List all tasks for a user.

**Parameters:**
- status: "all" | "pending" | "completed" (optional, default: "all")
- sort: "created" | "title" | "due_date" (optional, default: "created")
- limit: number (optional, default: 50)
- offset: number (optional, default: 0)

**Response (200 OK):**
```json
{
  "tasks": [
    {
      "id": "integer",
      "user_id": "string (UUID)",
      "title": "string (1-100 chars)",
      "description": "string (max 1000 chars)",
      "completed": "boolean",
      "created_at": "datetime",
      "updated_at": "datetime",
      "due_date": "datetime (nullable)",
      "recurrence_pattern": "string (nullable)"
    }
  ],
  "total_count": "number",
  "has_more": "boolean"
}
```

#### POST /api/{user_id}/tasks
Create a new task.

**Request Body:**
```json
{
  "title": "string (1-100 chars)",
  "description": "string (max 1000 chars, optional)",
  "due_date": "datetime (optional)",
  "recurrence_pattern": "string (optional, enum: daily, weekly, monthly, yearly, none)"
}
```

**Response (201 Created):**
```json
{
  "id": "integer",
  "user_id": "string (UUID)",
  "title": "string",
  "description": "string (nullable)",
  "completed": "boolean (default: false)",
  "created_at": "datetime",
  "updated_at": "datetime",
  "due_date": "datetime (nullable)",
  "recurrence_pattern": "string (nullable)"
}
```

**Response (400 Bad Request):**
- Title not provided or exceeds 100 characters
- Description exceeds 1000 characters
- Invalid recurrence pattern

#### GET /api/{user_id}/tasks/{id}
Get task details.

**Response (200 OK):**
```json
{
  "id": "integer",
  "user_id": "string (UUID)",
  "title": "string",
  "description": "string (nullable)",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime",
  "due_date": "datetime (nullable)",
  "recurrence_pattern": "string (nullable)"
}
```

**Response (404 Not Found):**
- Task does not exist or does not belong to user

#### PUT /api/{user_id}/tasks/{id}
Update a task.

**Request Body:**
```json
{
  "title": "string (1-100 chars)",
  "description": "string (max 1000 chars, optional)",
  "due_date": "datetime (optional)",
  "recurrence_pattern": "string (optional, enum: daily, weekly, monthly, yearly, none)"
}
```

**Response (200 OK):**
```json
{
  "id": "integer",
  "user_id": "string (UUID)",
  "title": "string",
  "description": "string (nullable)",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime",
  "due_date": "datetime (nullable)",
  "recurrence_pattern": "string (nullable)"
}
```

**Response (400 Bad Request):**
- Title exceeds 100 characters
- Description exceeds 1000 characters
- Invalid recurrence pattern

**Response (404 Not Found):**
- Task does not exist or does not belong to user

#### DELETE /api/{user_id}/tasks/{id}
Delete a task.

**Response (204 No Content):**
- Task successfully deleted

**Response (404 Not Found):**
- Task does not exist or does not belong to user

#### PATCH /api/{user_id}/tasks/{id}/complete
Toggle task completion status.

**Request Body:**
```json
{
  "completed": "boolean (required)"
}
```

**Response (200 OK):**
```json
{
  "id": "integer",
  "user_id": "string (UUID)",
  "title": "string",
  "description": "string (nullable)",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime",
  "due_date": "datetime (nullable)",
  "recurrence_pattern": "string (nullable)"
}
```

**Response (404 Not Found):**
- Task does not exist or does not belong to user

### Email Notifications

#### POST /api/notifications/email
Send an email notification for important events.

**Request Body:**
```json
{
  "to_email": "string (required)",
  "subject": "string (required)",
  "body": "string (required)"
}
```

**Response (200 OK):**
```json
{
  "success": "boolean",
  "message_id": "string (nullable)"
}
```

**Response (400 Bad Request):**
- Invalid email format
- Missing required fields