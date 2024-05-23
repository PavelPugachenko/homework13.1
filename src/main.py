class Category:
    def __init__(self, title, descriptions, products):
        self.title = title
        self.descriptions = descriptions
        self.__products = products

    @property
    def products(self):
        return [(f"{product.title}, {product.pay} руб. Остаток: {product.quantity} шт.") for product in self.__products]

    def get_total_category(self):
        total = 0
        for product in self.__products:
            total += product.pay * product.quantity
        self.total_category = total
        return total

    def add_product(self, product):
        self.__products.append(product)

class Product:
    def __init__(self, title, descriptions, pay, quantity):
        self.title = title
        self.descriptions = descriptions
        self.pay = pay
        self.quantity = quantity

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, new_pay):
        if new_pay <= 0:
            print("Цена введена некорректная")
        else:
            self.__pay = new_pay

    def get_total(self):
        return self.pay * self.quantity

    def update_quantity(self, update_quantity):
        self.quantity = update_quantity
        return self.quantity

    @staticmethod
    def create_product(title, descriptions, pay, quantity):
        return Product(title, descriptions, pay, quantity)
        return self.quantity