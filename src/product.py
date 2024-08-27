class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):


        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return  f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print('Price should be more than 0')
        elif self.__price > new_price:
            answer = input('Make price lower? [y/n]').lower()
            if answer == 'y':
                self.__price = new_price
            else:
                print('The price no has been changed')
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, new_product: dict, products_list: list):
        if products_list is None:
            return cls(**new_product)
        for product in products_list:
            if new_product["name"] == product.name:
                new_product["quantity"] += product.quantity
                if new_product["price"] < product.price:
                    new_product["price"] = product.price
        return cls(**new_product)


