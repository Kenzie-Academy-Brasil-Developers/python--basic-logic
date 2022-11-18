table_1 = [
    {"_id": 1, "amount": 5},
    {"_id": 19, "amount": 5}
]

table_2 = [
    {"_id": 10, "amount": 3},
    {"_id": 20, "amount": 2},
    {"_id": 21, "amount": 5},
]

product_mock = {
    "title": "X-Python",
    "price": 5.0,
    "rating": 5,
    "description": "Sanduiche de Python",
    "type": "fast-food"
}

required_keys = ("description", "price", "rating", "title", "type")

new_product = {
    "title": "X-Python",
    "price": 5.0,
    "rating": 5,
    "description": "Sanduiche de Python",
    "type": "fast-food",
    "extra_key_1": "extra_value_1",
    "extra_key_2": "extra_value_2"
}
