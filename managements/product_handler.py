from menu import products
from functools import reduce


def get_product_by_id(id: int = 0) -> dict:
    results = [product for product in products if product['_id'] == id]
    return results[0] if len(results) > 0 else []


def get_products_by_type(type: str = '') -> list:
    results = [product for product in products if product['type'] == type]
    return results


def menu_report() -> str:
    count = len(products)
    avg_price = sum(product['price'] for product in products) / count

    common_count = {}
    maximum = 0
    most_common = ''
    for product in products:
        if product['type'] not in common_count.keys():
            recurrence = len(get_products_by_type(product['type']))
            common_count.update({product['type']: recurrence})

            most_common = product['type'] if recurrence > maximum else most_common
            maximum = recurrence if recurrence > maximum else maximum

    return 'Products count: %i - Average price: %.2f - Most common type: %s' % (count, avg_price, most_common)
