def test_category_init(category_one, category_two):
    assert category_two.name == 'Moviles'
    assert category_two.description == 'Smartphones'
    assert category_one.name == 'Portatiles'
    assert category_one.description == 'Office Equipment and Supplies'

    assert len(category_one.products) == 5
    assert len(category_two.products) == 3
    assert category_two.categories_count == 2
    assert category_one.categories_count == 2


    assert category_two.all_quantity_products == 8
