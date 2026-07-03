from sqlalchemy import Column, Integer, String
from app.database.database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True)
    name = Column(String)
    department = Column(String)
    designation = Column(String)
    casual_leave = Column(Integer)
    sick_leave = Column(Integer)
    earned_leave = Column(Integer)