# Quickstart Guide: Full-Stack Todo Web Application

## Prerequisites
- Node.js 18+ (for Next.js frontend)
- Python 3.11+ (for FastAPI backend)
- PostgreSQL (or Neon Serverless PostgreSQL account)
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Backend Setup (FastAPI)
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your database and auth settings

# Run the backend server
uvicorn main:app --reload
```

### 3. Frontend Setup (Next.js)
```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set environment variables
cp .env.local.example .env.local
# Edit .env.local with your API and auth settings

# Run the development server
npm run dev
```

### 4. Environment Variables

#### Backend (.env)
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
BETTER_AUTH_SECRET=your-secret-key-here
BETTER_AUTH_URL=http://localhost:3000
```

#### Frontend (.env.local)
```env
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## Running the Application

### Development Mode
1. Start the backend server: `cd backend && uvicorn main:app --reload`
2. In a separate terminal, start the frontend: `cd frontend && npm run dev`
3. Access the application at http://localhost:3000

### Production Mode
1. Build the frontend: `cd frontend && npm run build`
2. Start the backend server with production settings
3. Serve the frontend build files

## Key Endpoints

### Frontend
- Home Page: `http://localhost:3000`
- Authentication: `http://localhost:3000/login`, `http://localhost:3000/register`
- Dashboard: `http://localhost:3000/dashboard`

### Backend API
- Base URL: `http://localhost:8000`
- Health Check: `GET /health`
- User Registration: `POST /api/auth/register`
- User Login: `POST /api/auth/login`
- Tasks: `GET/POST/PUT/DELETE /api/{user_id}/tasks/{id}`

## Testing

### Backend Tests
```bash
cd backend
python -m pytest
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## Database Migrations
```bash
cd backend
# Generate migration
alembic revision --autogenerate -m "Migration description"

# Apply migration
alembic upgrade head
```

## Troubleshooting

### Common Issues
1. **Port already in use**: Change ports in package.json (frontend) or uvicorn command (backend)
2. **Environment variables not loaded**: Ensure .env files are properly configured
3. **Database connection errors**: Verify DATABASE_URL is correct and database is running
4. **Authentication issues**: Check that BETTER_AUTH_SECRET is the same in both frontend and backend

### Resetting the Development Environment
```bash
# Backend
cd backend
deactivate  # Exit virtual environment
rm -rf venv  # Remove virtual environment
python -m venv venv  # Recreate virtual environment

# Frontend
cd frontend
rm -rf node_modules  # Remove node modules
npm install  # Reinstall dependencies
```