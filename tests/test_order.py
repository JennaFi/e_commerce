from src.order import Order


def test_order(product1):
    assert str(Order(product1, 2)) == "You've bought: Samsung Galaxy S23 Ultra - 2, the total price is 360000.0"