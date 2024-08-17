def test_product_init(product):
    assert product.name == 'Laptop Yoga'
    assert product.description == 'Processor 10'
    assert product.price == 780.90
    assert product.quantity == 5