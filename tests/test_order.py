import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization_and_validation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")

    with pytest.raises(TypeError):
        Order("not a customer", coffee, 3.0)
    with pytest.raises(TypeError):
        Order(customer, "not a coffee", 3.0)
    with pytest.raises(TypeError):
        Order(customer, coffee, "not a price")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)

    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0