def test_category(category_one, category_two, product4):
    assert category_two.name == 'Телевизоры'
    assert category_two.description == """Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"""
    assert category_one.name == 'Смартфоны'
    assert category_one.description == """Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"""

    assert category_two.categories_count == 2
    assert category_one.categories_count == 2


    assert category_two.all_quantity_products == 4

    assert category_one.products == ('Product: Samsung Galaxy S23 Ultra. Price: 180000.0. Quantity: 5.\n'
                                    'Product: Iphone 15. Price: 210000.0. Quantity: 8.\n'
                                    'Product: Xiaomi Redmi Note 11. Price: 31000.0. Quantity: 14.\n'
                                     )

    category_two.add_product(product4)
    assert category_two.all_quantity_products == 5
