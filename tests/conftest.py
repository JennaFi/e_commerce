import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_one():
    return Category(
        name='Portatiles',
        description='Office Equipment and Supplies',
        products=[Product('Laptop Yoga', 'Processor 10', 780.90, 5),
                Product('Laptop ASUS', 'Processor 25', 1090.90, 8),
                Product('Laptop Lenovo', 'Processor 45', 2044.60, 15),
                Product('Laptop HUAWEI', 'Processor 20', 1000.00, 7),
                Product('MacBook', 'Processor 45', 2500.80, 15)
                ]

    )
@pytest.fixture
def category_two():
    return Category(
        name='Moviles',
        description='Smartphones',
        products=[Product('iPhone', '15 MaxPro', 1100.20, 6),
                  Product('Galaxy', '(90UI)', 800.20, 10),
                  Product('Nokia', 'Sup890', 950.20, 8),

        ]

    )
@pytest.fixture
def product():
    return Product('Laptop Yoga', 'Processor 10', 780.90, 5)

