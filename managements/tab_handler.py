from menu import products


def calculate_tab(table: list[dict]):
    # {"_id": 10, "amount": 3}
    for order in table:
        for product in products:
            if product['_id'] == order['_id']:
                order.update({'price': product['price']})
    summary = sum([order['amount'] * order['price'] for order in table])
    return {'subtotal': '$%.2f' % summary}
