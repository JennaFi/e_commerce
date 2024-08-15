from src.product import Product


class Category:
    name: str
    description: str
    products: list
    categories_count = 0
    all_quantity_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.categories_count += 1
        Category.all_quantity_products += len(products)


