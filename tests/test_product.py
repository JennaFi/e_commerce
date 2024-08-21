from unittest.mock import patch

from src.product import Product


def test_product(capsys, product1, product2, product3, product4):
    assert product1.name == 'Samsung Galaxy S23 Ultra'
    assert product1.description == '256GB, Серый цвет, 200MP камера'
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == 'Iphone 15'
    assert product2.description == '512GB, Gray space'
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == 'Xiaomi Redmi Note 11'
    assert product3.description == '1024GB, Синий'
    assert product3.price == 31000.0
    assert product3.quantity == 14

    assert product4.name == '55" QLED 4K'
    assert product4.description == 'Фоновая подсветка'
    assert product4.price == 123000.0
    assert product4.quantity == 7

    product1.price = 200000.0
    assert product1.price == 200000.0
    product1.price = 0
    captured = capsys.readouterr()
    assert captured.out == 'Price should be more than 0\n'
    assert product1.price == 200000.0

    with patch('builtins.input') as mock_input:
        mock_input.return_value = 'y'
        product1.price = 100000.0
        assert product1.price == 100000.0

    with patch('builtins.input') as mock_input:
        mock_input.return_value = 'n'
        product1.price = 10
        captured = capsys.readouterr()
        assert captured.out == 'The price no has been changed\n'
        assert product1.price == 100000.0


def test_new_product(product1, product2, product3, product4):
    new_product = Product.new_product( {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Red цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }, [product1, product2, product3, product4])
    assert new_product.name == 'Samsung Galaxy S23 Ultra'

    new_product = Product.new_product({
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Red цвет, 200MP камера",
            "price": 160000.0,
            "quantity": 5,
        }, [product1, product2, product3, product4])
    assert new_product.quantity == 10
    assert new_product.price == 180000.0