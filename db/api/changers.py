from datetime import datetime
from sqlalchemy import Insert, Select, Update
from sqlalchemy.orm import Session
from wbapi.fetchers import fetch_sales_from_wb
from db import engine
from db.models import SalesItem


def prepare_sales_data(json_data):
    # '2023-06-30T04:16:43'
    format_string = '%Y-%m-%dT%H:%M:%S'
    json_data['date'] = datetime.strptime(json_data['date'], format_string)
    json_data['lastChangeDate'] = datetime.strptime(json_data['lastChangeDate'], format_string)


def get_sale_item_from_json(data: dict):
    return SalesItem(
        sale_id=data["saleID"],
        g_number=data["gNumber"],
        date=data["date"],
        last_change_date=data["lastChangeDate"],
        supplier_aticle=data["supplierArticle"],
        tech_size=data["techSize"],
        barcode=data["barcode"],
        total_price=data["totalPrice"],
        discount_percent=data["discountPercent"],
        is_supply=data["isSupply"],
        is_realization=data["isRealization"],
        promo_code_discount=data["promoCodeDiscount"],
        warehouse_name=data["warehouseName"],
        country_name=data["countryName"],
        oblast_okrug_name=data["oblastOkrugName"],
        region_name=data["regionName"],
        income_id=data["incomeID"],
        odid=data["odid"],
        spp=data["spp"],
        for_pay=data["forPay"],
        finished_price=data["finishedPrice"],
        price_with_disc=data["priceWithDisc"],
        nm_id=data["nmId"],
        subject=data["subject"],
        category=data["category"],
        brand=data["brand"],
        is_storno=data["IsStorno"],
        sticker=data["sticker"],
        srid=data["srid"]
        )


def record_exist(sale_id: str) -> bool:
    statement = Select(SalesItem).where(SalesItem.sale_id == sale_id)
    with Session(bind=engine) as session:
        return session.execute(statement=statement).first() is not None


def record_insert(data: list[SalesItem]):
    if len(data) == 0:
        return
    with Session(bind=engine) as session:
        session.add_all(data)
        session.commit()


def record_update(data: list[SalesItem]):
    if len(data) == 0:
        return
    with Session(bind=engine) as session:
        session.bulk_save_objects(data, update_changed_only=True)


def update_sales(date_from: str):
    sales = fetch_sales_from_wb(date_from=date_from)

    to_insert = []
    to_update = []
    for sale in sales:
        sale_id = sale.get("saleID", "")
        prepare_sales_data(sale)
        sale_item = get_sale_item_from_json(sale)

        if record_exist(sale_id=sale_id):
            to_update.append(sale_item)
        else:
            to_insert.append(sale_item)

    record_update(to_update)
    record_insert(to_insert)
