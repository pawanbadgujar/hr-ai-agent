from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate


class EmployeeService:

    @staticmethod
    def create_employee(db: Session, employee: EmployeeCreate):

        db_employee = Employee(
            employee_id=employee.employee_id,
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email,
            phone=employee.phone,
            department=employee.department,
            designation=employee.designation,
            joining_date=employee.joining_date,
        )

        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)

        return db_employee

    @staticmethod
    def get_all_employees(db: Session):

        return db.query(Employee).all()

    @staticmethod
    def get_employee_by_id(db: Session, employee_id: int):

        return (
            db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )