from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import DB_DRIVER


engine = create_engine(DB_DRIVER, echo=True)
session = Session(bind=engine)

__all__ = ["engine", "session"]
