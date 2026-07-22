from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    department = Column(String)
    designation = Column(String)
    joining_date = Column(Date)
    status = Column(String, default="Active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())