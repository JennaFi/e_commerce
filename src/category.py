from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    categories_count = 0
    all_quantity_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.categories_count += 1
        Category.all_quantity_products += len(products)

    @property
    def products(self):
        product_str = ''
        for product in self.__products:
            product_str += f"Product: {product.name}. Price: {product.price}. Quantity: {product.quantity}.\n"
        return product_str

    @property
    def products_list(self):
        return self.__products


    def add_product(self, product: Product):
        self.__products.append(product)
        Category.all_quantity_products += 1

