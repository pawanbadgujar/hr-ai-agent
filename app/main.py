from fastapi import FastAPI
from app.database.init_db import init_db
from app.routers.leave import router as leave_router

app = FastAPI(
    title="HR AI Agent",
    description="AI-powered HR Assistant for Leave, Payroll, Jobs and Workforce Queries",
    version="1.0.0"
)

app.include_router(leave_router)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {
        "status": "success",
        "message": "🚀 HR AI Agent is running successfully!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }