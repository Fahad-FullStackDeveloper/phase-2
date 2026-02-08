from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from routes
sys.path.append(str(Path(__file__).parent))

# Temporarily mock the routes to avoid model import issues
from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["Authentication"])
task_routes = APIRouter(prefix="/tasks", tags=["Tasks"])

# Define some basic endpoints
@auth_routes.get("/register")
def register():
    return {"message": "Registration endpoint (mock)"}

@auth_routes.get("/login")
def login():
    return {"message": "Login endpoint (mock)"}

@task_routes.get("/")
def get_tasks():
    return {"message": "Get tasks endpoint (mock)"}

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Todo API",
    description="RESTful API for the Full-Stack Todo Web Application",
    version="1.3.1"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes)
app.include_router(task_routes)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)