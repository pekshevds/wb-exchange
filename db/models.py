from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Numeric, DateTime, Boolean, Integer


class Base(DeclarativeBase):
    pass


class SalesItem(Base):
    __tablename__ = "sales_items"

    sale_id = mapped_column(String(length=15), name="saleID", primary_key=True)
    g_number = mapped_column(String(length=50), name="gNumber")
    date = mapped_column(DateTime, name="date")
    last_change_date = mapped_column(DateTime, name="lastChangeDate")
    supplier_aticle = mapped_column(String(length=75), name="supplierArticle")
    tech_size = mapped_column(String(length=30), name="techSize")
    barcode = mapped_column(String(length=30), name="barcode")
    total_price = mapped_column(Numeric, name="totalPrice")
    discount_percent = mapped_column(Integer, name="discountPercent")
    is_supply = mapped_column(Boolean, name="isSupply")
    is_realization = mapped_column(Boolean, name="isRealization")
    promo_code_discount = mapped_column(Numeric, name="promoCodeDiscount")
    warehouse_name = mapped_column(String(length=50), name="warehouseName")
    country_name = mapped_column(String(length=200), name="countryName")
    oblast_okrug_name = mapped_column(String(length=200), name="oblastOkrugName")
    region_name = mapped_column(String(length=200), name="regionName")
    income_id = mapped_column(Integer, name="incomeID")
    odid = mapped_column(Integer, name="odid")
    spp = mapped_column(Numeric, name="spp")
    for_pay = mapped_column(Numeric, name="forPay")
    finished_price = mapped_column(Numeric(), name="finishedPrice")
    price_with_disc = mapped_column(Numeric(), name="priceWithDisc")
    nm_id = mapped_column(Integer, name="nmId")
    subject = mapped_column(String(length=50), name="subject")
    category = mapped_column(String(length=50), name="category")
    brand = mapped_column(String(length=50), name="brand")
    is_storno = mapped_column(Integer, name="IsStorno")
    sticker = mapped_column(String, name="sticker")
    srid = mapped_column(String, name="srid")
