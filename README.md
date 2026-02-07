# Todo Full-Stack Web Application

This is a modern multi-user todo application built with Next.js 16+ frontend and Python FastAPI backend, featuring persistent storage in Neon Serverless PostgreSQL and authentication via Better Auth.

## Getting Started

### Prerequisites

- Node.js 18+ (for Next.js frontend)
- Python 3.11+ (for FastAPI backend)
- Neon PostgreSQL account for database

### Frontend Setup

First, run the development server for the frontend:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Backend Setup

For the backend, navigate to the backend directory and run:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## Technology Stack

- **Frontend**: Next.js 16.1.6 (App Router), TypeScript, Tailwind CSS
- **Backend**: Python FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT integration
- **Spec-Driven Development**: Claude Code + Spec-Kit Plus

## API Endpoints

The application provides the following RESTful API endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/{user_id}/tasks` | List all tasks for a user |
| POST | `/api/{user_id}/tasks` | Create a new task |
| GET | `/api/{user_id}/tasks/{id}` | Get task details |
| PUT | `/api/{user_id}/tasks/{id}` | Update a task |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete a task |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle task completion |

## Authentication

The application uses Better Auth with JWT tokens for secure communication between frontend and backend. All API requests must include a valid JWT token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

## Development Workflow

This project follows the Agentic Dev Stack workflow:
1. Write spec → Generate plan → Break into tasks → Implement via Claude Code
2. Specifications are located in the `specs/` directory
3. All development must comply with the constitutional principles in `.specify/memory/constitution.md`

## Learn More

To learn more about the technologies used in this project:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - modern, fast, web framework for building APIs with Python
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/) - SQL databases in Python, with Python types
- [Better Auth Documentation](https://better-auth.com/) - authentication library for modern web applications
- [Neon Documentation](https://neon.tech/docs) - serverless PostgreSQL

## Deploy on Vercel

The frontend can be deployed on Vercel, while the backend can be deployed on platforms supporting Python applications. The database uses Neon Serverless PostgreSQL for automatic scaling.
