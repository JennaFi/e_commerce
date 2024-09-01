import pytest


def test_lawn_grass_init(lawngrass_1):
    assert lawngrass_1.colour == "Зеленый"


def test_lawn_grass_add(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 16750


def test_lawn_grass_add_error(lawngrass_1, product2):
    with pytest.raises(TypeError):
        assert lawngrass_1 + product2