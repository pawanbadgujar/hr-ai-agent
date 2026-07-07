from fastapi import APIRouter
from app.services.workforce_service import WorkforceService

router = APIRouter(
    prefix="/workforce",
    tags=["Workforce"]
)


@router.get("/management")
def workforce_management():
    return WorkforceService.get_workforce_management()