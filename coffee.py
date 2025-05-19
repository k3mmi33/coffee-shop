class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters.")
        self._name = value

    def add_order(self, order):
        self.orders.append(order)

    def customers(self):
        return list({order.customer for order in self.orders})

    def __repr__(self):
        return f"<Coffee {self.name}>"