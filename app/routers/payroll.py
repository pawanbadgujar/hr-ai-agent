from fastapi import APIRouter
from app.services.payroll_service import PayrollService

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


@router.get("/basics")
def payroll_basics():
    return PayrollService.get_payroll_basics()