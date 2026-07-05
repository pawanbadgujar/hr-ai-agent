from fastapi import APIRouter
from app.services.leave_service import LeaveService

router = APIRouter(
    prefix="/leave",
    tags=["Leave"]
)


@router.get("/process")
def leave_process():
    return {
        "process": LeaveService.get_leave_process()
    }


@router.get("/policy")
def leave_policy():
    return LeaveService.get_leave_policy()