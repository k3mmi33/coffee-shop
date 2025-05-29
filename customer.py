class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders.copy()

    def coffees(self):
        unique_coffees = []
        for order in self._orders:
            coffee = order.coffee
            if coffee not in unique_coffees:
                unique_coffees.append(coffee)
        return unique_coffees

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        from collections import defaultdict
        spending = defaultdict(float)
        for order in coffee.orders():
            spending[order.customer] += order.price
        if not spending:
            return None
        max_customer = max(spending, key=spending.get)
        return max_customer