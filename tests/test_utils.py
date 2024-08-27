from unittest.mock import mock_open, patch

from src.utils import reading_json, loading_products_from_json


def test_read_json():
    m = mock_open(read_data="""{"test_key": "test_value"}""")
    with patch("builtins.open", m):
        assert reading_json("test_path") == {"test_key": "test_value"}

def test_create_products_by_categories_from_dict(products_by_category):
    categories_list = loading_products_from_json(products_by_category)
    assert categories_list[0].name == "Смартфоны"
    assert (
        categories_list[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert categories_list[0].products_list[0].name == "Samsung Galaxy C23 Ultra"
    assert categories_list[0].products_list[1].description == "512GB, Gray space"
    assert categories_list[0].products_list[2].price == 31000.0
    assert categories_list[1].products_list[0].quantity == 7