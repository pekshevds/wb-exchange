from sqlalchemy import create_engine
from config import DB_DRIVER


engine = create_engine(DB_DRIVER, echo=True)

__all__ = ["engine"]
