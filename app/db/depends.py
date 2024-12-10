
from sqlalchemy.orm import Session
from app.db.connection import Session




def get_db():
    try:
        session = Session()
        yield session
    finally:
        session.close()


