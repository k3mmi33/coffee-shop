from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer.add_order(self)
        coffee.add_order(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer must be a Customer instance.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("price must be a number.")
        if not (1.0 <= value <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0.")
        self._price = value

    def __repr__(self):
        return f"<Order {self.customer.name} - {self.coffee.name} - ${self.price:.2f}>"