class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

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

    def add_order(self, order):
        self.orders.append(order)

    def coffees(self):
        return list({order.coffee for order in self.orders})

    def total_money_spent(self):
        return sum(order.price for order in self.orders)

    def __repr__(self):
        return f"<Customer {self.name}>"