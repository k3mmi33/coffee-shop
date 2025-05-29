import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

def test_edge_cases_and_exceptions():
    # Customer name edge cases
    with pytest.raises(TypeError):
        Customer(None)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)

    # Coffee name edge cases
    with pytest.raises(TypeError):
        Coffee(None)
    with pytest.raises(ValueError):
        Coffee("ab")

    # Order price edge cases
    customer = Customer("TestUser")
    coffee = Coffee("TestCoffee")
    with pytest.raises(TypeError):
        Order(customer, coffee, "price")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.99)
    with pytest.raises(ValueError):
        Order(customer, coffee, 10.01)

def test_multiple_orders_and_relationships():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    o1 = c1.create_order(coffee1, 3.0)
    o2 = c1.create_order(coffee2, 4.0)
    o3 = c2.create_order(coffee1, 5.0)
    o4 = c2.create_order(coffee2, 6.0)
    o5 = c2.create_order(coffee2, 7.0)

    # Check orders count
    assert len(c1.orders()) == 2
    assert len(c2.orders()) == 3
    assert coffee1.num_orders() == 2
    assert coffee2.num_orders() == 3

    # Check unique coffees for customers
    assert set(c1.coffees()) == {coffee1, coffee2}
    assert set(c2.coffees()) == {coffee1, coffee2}

    # Check unique customers for coffees
    assert set(coffee1.customers()) == {c1, c2}
    assert set(coffee2.customers()) == {c1, c2}

    # Check average price calculations
    assert coffee1.average_price() == (3.0 + 5.0) / 2
    assert coffee2.average_price() == (4.0 + 6.0 + 7.0) / 3

def test_debug_script_usage(monkeypatch):
    # This test simulates running debug.py main function
    import debug

    # Monkeypatch print to capture outputs
    outputs = []
    def fake_print(*args, **kwargs):
        outputs.append(args)

    monkeypatch.setattr("builtins.print", fake_print)
    debug.main()

    # Check some expected outputs in captured prints
    found_alice_orders = any("Alice's orders:" in str(o) for o in outputs)
    found_espresso_orders = any("Espresso orders count:" in str(o) for o in outputs)
    found_most_aficionado = any("Most aficionado for Espresso:" in str(o) for o in outputs)

    assert found_alice_orders
    assert found_espresso_orders
    assert found_most_aficionado