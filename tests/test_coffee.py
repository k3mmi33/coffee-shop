import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    c = Coffee("Mocha")
    assert c.name == "Mocha"

def test_orders_customers_num_orders_average_price():
    coffee = Coffee("Latte")
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    o1 = c1.create_order(coffee, 4.0)
    o2 = c2.create_order(coffee, 6.0)
    assert o1 in coffee.orders()
    assert o2 in coffee.orders()
    customers = coffee.customers()
    assert c1 in customers and c2 in customers
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0

def test_average_price_no_orders():
    coffee = Coffee("Espresso")
    assert coffee.average_price() == 0.0