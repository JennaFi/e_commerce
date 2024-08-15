import json
import os

from src.category import Category
from src.product import Product


def reading_json(path) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def loading_products_from_json(data: dict):
    categories = []
    for category in data:

        products_list = []

        for product in category["products"]:

            products_list.append(Product(**product))

        category["products"] = products_list

        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    raw_data = reading_json('../data/products.json')
    products_loaded = loading_products_from_json(raw_data)
    print(products_loaded)