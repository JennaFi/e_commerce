def test_category(category_one, category_two, product4):
    assert category_two.name == 'Телевизоры'
    assert category_two.description == """Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"""
    assert category_one.name == 'Смартфоны'
    assert category_one.description == """Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"""

    assert category_two.categories_count == 2
    assert category_one.categories_count == 2


    assert category_two.product_count == 4

    assert category_one.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                    'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                    'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'
                                     )

    category_two.add_product(product4)
    assert category_two.product_count == 5
