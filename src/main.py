class Category:
    def __init__(self, title, descriptions, products):
        self.title = title
        self.descriptions = descriptions
        self.__products = products
    def __len__(self):
        return len(self.products)
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
    def __str__(self):
        return f'Название категории, количество продуктов: {len(self)} шт.'

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

    def __add__(self, other):
        total_price_self = self.pay * self.quantity
        total_price_other = other.pay * other.quantity
        return total_price_self + total_price_other

    def get_total(self):
        return self.pay * self.quantity

    def update_quantity(self, update_quantity):
        self.quantity = update_quantity
        return self.quantity

    @classmethod
    def create_product(cls, title, descriptions, pay, quantity):
        return cls(title, descriptions, pay, quantity)

    def __str__(self):
        return f'{self.title}, {self.pay} руб. Остаток: {self.quantity} шт.'

