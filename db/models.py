from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Numeric, DateTime, Boolean, Integer


class Base(DeclarativeBase):
    pass

class SalesItem(Base):
    __tablename__ = "sales_items"

    sale_id = mapped_column("saleID", String(length=15), primary_key=True)
    g_number = mapped_column("gNumber", String(length=50))
    date = mapped_column("date", DateTime)
    last_change_date = mapped_column("lastChangeDate", DateTime)
    supplier_aticle = mapped_column("supplierArticle", String(length=75))
    tech_size = mapped_column("techSize", String(length=30))
    barcode = mapped_column("barcode", String(length=30))
    total_price = mapped_column("totalPrice", Numeric())
    discount_percent = mapped_column("discountPercent", Integer())
    is_supply = mapped_column("isSupply", Boolean())
    is_realization = mapped_column("isRealization", Boolean())
    promo_code_discount = mapped_column("promoCodeDiscount", Numeric())
    warehouse_name = mapped_column("warehouseName", String(length=50))
    country_name = mapped_column("countryName", String(length=200))
    oblast_okrug_name = mapped_column("oblastOkrugName", String(length=200))
    region_name = mapped_column("regionName", String(length=200))
    income_id = mapped_column("incomeID", Integer())
    odid = mapped_column("odid", Integer())
    spp = mapped_column("spp", Numeric())
    for_pay = mapped_column("forPay", Numeric())
    finished_price = mapped_column("finishedPrice", Numeric())
    price_with_disc = mapped_column("priceWithDisc", Numeric())
    nm_id = mapped_column("nmId", Integer())
    subject = mapped_column("subject", String(length=50))
    category = mapped_column("category", String(length=50))
    brand = mapped_column("brand", String(length=50))
    is_storno = mapped_column("isStorno", Boolean())
    sticker = mapped_column("sticker", String())
    srid = mapped_column("srid", String())

    