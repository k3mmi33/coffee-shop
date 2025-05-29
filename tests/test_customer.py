import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)
    c = Customer("Alice")
    assert c.name == "Alice"

def test_create_order_and_relationships():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert order in customer.orders()
    assert coffee in customer.coffees()

def test_most_aficionado():
    coffee = Coffee("Espresso")
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    c1.create_order(coffee, 3.0)
    c1.create_order(coffee, 4.0)
    c2.create_order(coffee, 5.0)
    assert Customer.most_aficionado(coffee) == c1
    empty_coffee = Coffee("Mocha")
    assert Customer.most_aficionado(empty_coffee) is None