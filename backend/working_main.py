from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

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

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API - Backend is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "todo-api"}

# Mock endpoints to replace the actual routes
@app.post("/auth/register")
def mock_register():
    return {"message": "Mock registration endpoint"}

@app.post("/auth/login")
def mock_login():
    return {"message": "Mock login endpoint"}

@app.get("/tasks")
def mock_get_tasks():
    return {"message": "Mock get tasks endpoint"}

@app.post("/tasks")
def mock_create_task():
    return {"message": "Mock create task endpoint"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)