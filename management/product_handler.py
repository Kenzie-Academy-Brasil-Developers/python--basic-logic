from menu import products
from utils import gen_id


def get_product_by_id(id: int = 0) -> (dict | str):
    if type(id) != int:
        raise TypeError('product id must be an int')
    try:
        results = [product for product in products if product['_id'] == id]
        return results[0]
    except IndexError:
        return {}


def get_products_by_type(prodType: str = '') -> (list | str):
    if type(prodType) != str:
        raise TypeError('product type must be a str')

    results = [product for product in products if product['type'] == prodType]
    return results


def menu_report() -> str:
    count = len(products)
    avg_price = sum(product['price'] for product in products) / count

    data = {'types': [], 'most_common': '', 'recurrence': 0}
    for product in products:
        if product['type'] not in data['types']:
            recurrence = len(get_products_by_type(product['type']))
            data.update({
                'types': [*data['types'], product['type']],
                'most_common': product['type'] if recurrence > data['recurrence'] else data['most_common'],
                'recurrence': recurrence if recurrence > data['recurrence'] else data['recurrence']
            })
    most_common = data['most_common']
    return f'Products Count: {count} - Average Price: ${round(avg_price, 2)} - Most Common Type: {most_common}'


def add_product(menu: list, **kwargs) -> dict[str: (str | float)]:
    new_id = gen_id(menu)
    new_product = {'_id': new_id, **kwargs}
    menu.append(new_product)

    return new_product


def add_product_extra(menu: list, *requiredKeys: list[str], **kwargs) -> dict[str: (str | float)]:
    for key in requiredKeys:
        if key not in kwargs.keys():
            absent_key = key
            raise KeyError('field %s is required' % absent_key)
        new_id = gen_id(menu)

    valid_args = {key: arg for key, arg in kwargs.items() if key in requiredKeys}

    new_product = {'_id': new_id, **valid_args}
    menu.append(new_product)

    return new_product
