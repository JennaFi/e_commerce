def test_category(capsys, category_one, category_two, product4):
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
    message = capsys.readouterr()
    assert category_two.product_count == 5
    assert message.out.strip().split("\n")[-2] == "Товар успешно добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"


def test_category_str(category_one):
    assert str(category_one) == 'Смартфоны, количество продуктов: 27 шт.'


def test_middle_total_price(category_one, category_without_products):
    assert category_one.total_middle_price() == 140333.33
    assert category_without_products.total_middle_price() == 0


def test_custom_exception(capsys, category_one, category_two, product4):
    product4.quantity = 0
    category_two.add_product(product4)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар с нулевым количеством добавить нельзя"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"


# def test_add_product_error(category_two):