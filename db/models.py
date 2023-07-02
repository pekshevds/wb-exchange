from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Numeric, DateTime, Boolean


class Base(DeclarativeBase):
    pass

class SalesItem(Base):
    __tablename__ = "sales_items"

    sale_id = mapped_column("saleID", String(length=15), primary_key=True)
    g_number = mapped_column("gNumber", String(length=50))
    