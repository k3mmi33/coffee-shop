from customer import Customer
from coffee import Coffee

def main():
    alice = Customer("Alice")
    bob = Customer("Bob")

    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    alice.create_order(espresso, 3.5)
    alice.create_order(latte, 4.0)
    bob.create_order(espresso, 3.0)

    print(f"Alice's orders: {[order.coffee.name for order in alice.orders()]}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")

    print(f"Espresso orders count: {espresso.num_orders()}")
    print(f"Espresso average price: {espresso.average_price():.2f}")
    print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")

    aficionado = Customer.most_aficionado(espresso)
    if aficionado:
        print(f"Most aficionado for Espresso: {aficionado.name}")
    else:
        print("No aficionado for Espresso")

if __name__ == "__main__":
    main()