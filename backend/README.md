# Backend API for Todo Application

This is the backend API for the Todo Full-Stack Web Application, built with FastAPI and Python.

## Features

- User authentication and registration
- Task management (CRUD operations)
- Recurring tasks functionality
- Email notifications
- JWT-based authentication

## Tech Stack

- Python 3.11+
- FastAPI 0.115+
- SQLModel for database operations
- Pydantic for data validation
- Better Auth for authentication
- Neon Serverless PostgreSQL for database

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database connection details and auth secrets
   ```

3. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

## API Endpoints

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /tasks` - Get user's tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task
- `PATCH /tasks/{id}/complete` - Toggle task completion

## Testing

Run the tests using pytest:

```bash
pytest
```