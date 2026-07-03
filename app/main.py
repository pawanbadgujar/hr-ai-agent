from fastapi import FastAPI

app = FastAPI(
    title="HR AI Agent",
    description="AI-powered HR Assistant for Leave, Payroll, Jobs and Workforce Queries",
    version="1.0.0"
)


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