'''Create a class Called Order which stores item and its price.
USe Dunder function __gt__() to convey that:
order1 > order2 if price of order 1 > price of order 2'''

class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price
    

order1 = Order("Chips", 20)
order2 = Order("Beer", 180)

print(order1 > order2)