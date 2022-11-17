from managements import get_product_by_id, get_products_by_type, menu_report

if __name__ == "__main__":
    # Seus prints de teste aqui
    find_id = get_product_by_id(28)
    # print(find_id)

    find_type = get_products_by_type('drink')
    # print(find_type)

    report = menu_report()
    print(report)
