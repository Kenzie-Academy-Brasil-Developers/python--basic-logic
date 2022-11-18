def generate_sequencial_id(list: list):
    generated_id = 1
    for item in list:
        next_id = item['_id']
        generated_id = next_id if item['_id'] > generated_id else generated_id
    if generated_id > 1:
        generated_id += 1

    return generated_id
