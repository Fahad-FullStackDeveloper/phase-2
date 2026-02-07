# Quickstart Guide: Full-Stack Todo Web Application

## Prerequisites

- Node.js 18+ with npm/yarn
- Python 3.11+
- PostgreSQL (or Neon Serverless PostgreSQL account)
- Git

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Backend Setup (Python FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database connection details and auth secrets
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the backend server:
   ```bash
   uvicorn src.main:app --reload
   ```

### 3. Frontend Setup (Next.js)

1. Navigate to the frontend directory:
   ```bash
   cd frontend  # or if it's in the root directory
   cd .
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your API endpoint and auth configuration
   ```

4. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

## Environment Variables

### Backend (.env)
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
BETTER_AUTH_SECRET=your-super-secret-jwt-key-here
BETTER_AUTH_URL=http://localhost:3000
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
```

## Running the Application

1. Start the backend server (port 8000 by default)
2. Start the frontend server (port 3000 by default)
3. Access the application at http://localhost:3000

## API Endpoints

Once running, the API will be available at `http://localhost:8000/api` with the following key endpoints:

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /tasks` - Get user's tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

## Testing

### Backend Tests
```bash
cd backend
source venv/bin/activate
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
# or
yarn test
```

## Deployment

### Backend
The backend is designed to work with any Python WSGI/ASGI hosting service. Configure your production environment variables appropriately.

### Frontend
The Next.js frontend can be deployed to Vercel, Netlify, or any hosting service that supports Next.js applications.

## Troubleshooting

- If you encounter database connection issues, verify your `DATABASE_URL` is correct
- For authentication problems, ensure `BETTER_AUTH_SECRET` is the same in both frontend and backend
- If API calls fail, check that your `NEXT_PUBLIC_API_BASE_URL` points to the correct backend address