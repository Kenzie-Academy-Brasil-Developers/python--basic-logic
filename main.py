from menu import products
from mocks import *
from managements import *

if __name__ == "__main__":
    # Seus prints de teste aqui
    ...
    # id
    # print(get_product_by_id(28))                                      # id existente
    # print(get_product_by_id(456))                                     # id inexistente
    # print(get_product_by_id([1, 2, 3]))                               # parametro id inválido

    # type
    # print(get_products_by_type('drink'))                              # tipo existente
    # print(get_products_by_type('inexistente'))                        # tipo inexistente
    # print(get_products_by_type([1, 2, 3, 4]))                         # tipo inválido

    # report
    # print(menu_report())                                              # datlhes

    # add products
    # print(add_product(products, **product_mock))                      # adicionar novo produto
    # print(add_product(empty_list, **product_mock))                    # adicionar novo produto a uma lista vazia

    # calculate subtotal
    # print(calculate_tab(table_1))                                     # calculo de subtotal
    # print(calculate_tab(table_2))                                     # calculo de subtotal

    # add products extra
    # print(add_product_extra(products, *required_keys, **new_product)) # DESAFIO EXTRA
