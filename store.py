__author__ = 'Beni'


class Store(object):
    def __init__(self):
        self.inventory = {
            "Bread":   {"price": 2, "quantity": 5},
            "Milk":    {"price": 1, "quantity": 10}
        }
        self.customers = []
        self.money = 0

    def stock(self, name):
        self.inventory =



class Customer(object):
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.cart = []

    def buy(self, item):
        self.balance = self.balance - 2
        self.cart.append(item)


cust1 = Customer()

cust1.buy("bread")

if "Bread" in n_store.inventory:
    item = n_store.inventory.get("Bread")

print cust1

