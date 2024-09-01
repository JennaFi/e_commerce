from src.product import Product


class LawnGrass(Product):
    def __init__(self,name, description, price, quantity, country, germination_period, colour):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.colour = colour

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError



