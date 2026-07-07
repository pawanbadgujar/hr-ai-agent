from fastapi import FastAPI
from app.routers.leave import router as leave_router
from app.routers import jobs
from app.routers import payroll
from app.routers import workforce
from app.routers import chatbot


app = FastAPI(
    title="HR AI Agent",
    description="AI-powered HR Assistant for Leave, Payroll, Jobs and Workforce Queries",
    version="1.0.0"
)

app.include_router(leave_router)
app.include_router(jobs.router)
app.include_router(payroll.router)
app.include_router(workforce.router)
app.include_router(chatbot.router)

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