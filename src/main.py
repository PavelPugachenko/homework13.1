class Category:
    def __init__(self, title, descriptions, products):
        self.title = title
        self.descriptions = descriptions
        self.products = products

    def get_total_category(self):
        total = 0
        for product in self.products:
            total += product.pay * product.quantity
        self.total_category = total
        return total

class Product:
    def __init__(self, title, descriptions, pay, quantity):
        self.title = title
        self.descriptions = descriptions
        self.pay = pay
        self.quantity = quantity

    def get_total(self):
        return self.pay * self.quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        return self.quantity


