import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == 'Samsung Galaxy S23 Ultra'
    assert smartphone_1.description == '256GB, Серый цвет, 200MP камера'
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == 'S23 Ultra'
    assert smartphone_1.memory == 256
    assert smartphone_1.colour == 'Серый'

def test_smartphone_add(smartphone_2, smartphone_3):
    assert smartphone_2 + smartphone_3 == 2114000

def test_smartphone_add_error(smartphone_1, product2):
    with pytest.raises(TypeError):
        assert smartphone_1 + product2