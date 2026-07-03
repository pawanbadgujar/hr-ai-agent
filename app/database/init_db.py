from app.database.database import Base, engine

# Import all models here
from app.models.employee import Employee


def init_db():
    Base.metadata.create_all(bind=engine)