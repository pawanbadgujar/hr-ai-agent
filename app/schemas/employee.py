from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    employee_id: str
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    joining_date: Optional[date] = None


class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    phone: Optional[str]
    department: Optional[str]
    designation: Optional[str]
    joining_date: Optional[date]
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }