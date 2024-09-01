from src.product import Product


class Order:
    product: Product
    amount: int
    total_price: float

    def __init__(self, product: Product, amount: int):
        self.product = product
        self.amount = amount
        self.total_price = self.product.price * self.amount
        self.product.quantity -= self.amount

    def __str__(self) -> str:
        return f"You've bought: {self.product.name} - {self.amount}, the total price is {self.total_price}"