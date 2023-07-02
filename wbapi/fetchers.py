from requests import get, Response, RequestException
from config import WB_STATISTIC_KEY


def get_connection(date_from: str, flag: int = 0) -> Response:
    """
    Дата в формате RFC3339. Можно передать дату или дату со временем.
    Время можно указывать с точностью до секунд или миллисекунд.
    Литера Z в конце строки означает, что время передается в UTC-часовом поясе.
    При ее отсутствии время считается в часовом поясе МСК (UTC+3).
    Примеры:

    2019-06-20 "%Y-%m-%d"
    2019-06-20T00:00:00Z
    2019-06-20T23:59:59
    2019-06-20T00:00:00.12345Z
    2019-06-20T00:00:00.12345
    2017-03-25T00:00:00"""
    headers = {
        'Authorization': WB_STATISTIC_KEY,
        'Content-Type': 'application/json'
        }
    url = f"https://statistics-api.wildberries.ru/api/v1/supplier/sales?dateFrom={date_from}&flag={flag}"

    try:
        response = get(url, headers=headers)
    except RequestException:
        return None
    return response


def fetch_sales_from_wb(date_from: str, flag: int = 0) -> list:
    response = get_connection(date_from=date_from, flag=flag)
    if response and response.ok:
        return response.json()
    return []


if __name__ == "__main__":
    pass

__all__ = ["fetch_sales_from_wb"]
