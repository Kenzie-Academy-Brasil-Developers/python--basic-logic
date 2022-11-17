from menu import products
from functools import reduce


def get_product_by_id(id: int = 0) -> dict:
    result = list(filter(lambda product: product['_id'] == id, products))
    return {} if len(result) < 1 else result[0]


def get_products_by_type(type: str = ''):
    result = list(filter(lambda product: product['type'] == type, products))
    return [] if len(result) < 1 else result


def menu_report():
    inventory = len(products)

    product_prices = map(lambda product: product['price'], products)
    total_price = reduce(lambda a, b: a + b, product_prices)
    avg_price = total_price / inventory

    type_keys: list = []
    maximum: int = 0
    for product in products:
        if product['type'] not in type_keys:
            type_keys.append(product['type'])
            item_count = len(get_products_by_type(product['type']))

            if maximum < item_count:
                maximum = item_count
                most_common = product['type']

    return 'Products count: %i - Average price: %.2f - Most common type: %s' % (inventory, avg_price, most_common)
