# Todo Full-Stack Web Application

This is a modern multi-user todo application built with Next.js 16+ frontend and Python FastAPI backend, featuring persistent storage in Neon Serverless PostgreSQL and authentication via Better Auth.

## Getting Started

### Prerequisites

- Node.js 18+ (for Next.js frontend)
- Python 3.11+ (for FastAPI backend)
- Neon PostgreSQL account for database

### Running the Application

To run both frontend and backend simultaneously:

```bash
npm run dev
```

This will start:
- Frontend on [http://localhost:3000](http://localhost:3000) (or alternate port if 3000 is busy)
- Backend API on [http://localhost:8000](http://localhost:8000)

Alternatively, you can run them separately:

#### Frontend Setup
```bash
cd frontend
npm run dev
```

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## Technology Stack

- **Frontend**: Next.js 16.1.6 (App Router), TypeScript, Tailwind CSS
- **Backend**: Python FastAPI 0.115+
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: JWT-based authentication with custom service
- **Spec-Driven Development**: Claude Code + Spec-Kit Plus
- **API Design**: RESTful endpoints with comprehensive contracts
- **Data Modeling**: Structured entities with validation rules
- **Documentation**: Implementation planning artifacts and quickstart guides
- **Task Management**: Actionable, dependency-ordered implementation tasks
- **Quality Assurance**: Requirements validation checklists
- **Implementation Strategy**: User story-based development with MVP approach
- **Cross-Artifact Analysis**: Consistency and quality validation across spec, plan, and tasks

## API Endpoints

The application provides the following RESTful API endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List all tasks for authenticated user |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{id}` | Get task details |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |
| PATCH | `/tasks/{id}/complete` | Toggle task completion |
| POST | `/auth/register` | User registration |
| POST | `/auth/login` | User login |

## Authentication

The application uses JWT tokens for secure communication between frontend and backend. All protected API requests must include a valid JWT token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

## Troubleshooting

### Common Issues and Solutions

1. **LightningCSS Module Error on Windows**:
   - If you encounter `Cannot find module '../lightningcss.win32-x64-msvc.node'` error:
   - Clear the Next.js cache: `rm -rf .next` (or `rmdir /s /q .next` on Windows)
   - Reinstall dependencies: `npm install`
   - Rebuild the project: `npm run build`

2. **Backend Dependency Issues**:
   - If you encounter module import errors, ensure all required packages are installed:
   - Navigate to the backend directory: `cd backend`
   - Install dependencies: `pip install -r requirements.txt`
   - If psycopg2-binary installation fails on Windows, install PostgreSQL client libraries or use alternative drivers

3. **API Connection Issues**:
   - Ensure the API_BASE_URL in `frontend/src/lib/api.ts` matches your backend server address
   - Default is set to `http://localhost:8000` without additional prefixes

## Development Workflow

This project follows the Agentic Dev Stack workflow:
1. Write spec → Generate plan → Break into tasks → Analyze consistency → Implement via Claude Code
2. Specifications are located in the `specs/` directory
3. All development must comply with the constitutional principles in `.specify/memory/constitution.md`
4. Cross-artifact consistency analysis ensures alignment between spec, plan, and tasks

## Features

- **User Registration & Authentication**: Secure user accounts with email/password
- **Task Management**: Create, read, update, and delete personal tasks
- **Recurring Tasks**: Automatic generation of new task instances based on recurrence patterns
- **Data Isolation**: Each user only sees their own tasks
- **Email Notifications**: Deadline reminders, task assignments, and account alerts
- **Responsive UI**: Works across different device sizes
- **Automatic Token Refresh**: Seamless background refresh of JWT tokens
- **Offline Mode**: Ability to work with tasks when disconnected from the internet (planned)
- **Password Reset & Account Recovery**: Self-service options for account access (planned)
- **API Rate Limiting**: Protection against abuse and ensuring fair usage (planned)

## Learn More

To learn more about the technologies used in this project:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - modern, fast, web framework for building APIs with Python
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/) - SQL databases in Python, with Python types
- [Tailwind CSS Documentation](https://tailwindcss.com/) - utility-first CSS framework
- [Neon Documentation](https://neon.tech/docs) - serverless PostgreSQL

## Deploy on Vercel

The frontend can be deployed on Vercel, while the backend can be deployed on platforms supporting Python applications. The database uses Neon Serverless PostgreSQL for automatic scaling.
