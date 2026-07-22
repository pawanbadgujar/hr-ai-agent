from fastapi import FastAPI
from app.routers.leave import router as leave_router
from app.routers import jobs
from app.routers import payroll
from app.routers import workforce
from app.routers import chatbot

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="HR AI Agent",
    description="AI-powered HR Assistant for Leave, Payroll, Jobs and Workforce Queries",
    version="1.0.0"
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

app.include_router(leave_router)
app.include_router(jobs.router)
app.include_router(payroll.router)
app.include_router(workforce.router)
app.include_router(chatbot.router)

# @app.get("/")
# def root():
#     return {
#         "status": "success",
#         "message": "🚀 HR AI Agent is running successfully!"
#     }

@app.get("/", include_in_schema=False)
def home():
    return FileResponse("frontend/index.html")

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)