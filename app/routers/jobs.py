from fastapi import APIRouter
from app.services.job_service import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/creation")
def job_creation():
    return JobService.get_job_creation_process()


@router.get("/requirements")
def job_requirements():
    return JobService.get_job_requirements()