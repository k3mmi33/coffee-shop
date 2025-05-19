from customer import Customer
from coffee import Coffee
from order import Order

# Sample data
alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

order1 = Order(alice, latte, 4.5)
order2 = Order(alice, mocha, 5.0)
order3 = Order(bob, latte, 4.5)

# Output tests
print(alice.coffees())         # [Latte, Mocha]
print(bob.coffees())           # [Latte]
print(latte.customers())       # [Alice, Bob]
print(alice.total_money_spent())  # 9.5