# from wbapi.fetchers import download_sales
from db.api.changers import update_sales

if __name__ == "__main__":

    update_sales("2023-07-01")
    """sales = download_sales("2023-06-25")
    for sale_item in sales:
        print(sale_item)"""
