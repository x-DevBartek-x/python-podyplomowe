# Główny plik aplikacji pizzerii - Weekend 2
# Pełna wersja z obsługą wyjątków i I/O

from pizza import Pizza, Menu
from customer import Customer, VIPCustomer, CustomerManager
from order import Order, OrderManager
from exceptions import (
    PizzeriaError,
    InvalidPriceError,
    PizzaNotFoundError,
    CustomerNotFoundError,
    EmptyOrderError
)


def main():
    """Główna funkcja aplikacji."""
    print("=" * 60)
    print("APLIKACJA PIZZERII - Weekend 2 (Wyjątki + I/O)")
    print("=" * 60)

    # Reset liczników dla czystego demo
    Customer.reset_id_counter()
    Order.reset_id_counter()

    # === WCZYTYWANIE DANYCH ===
    print("\n--- Wczytywanie danych ---")

    menu = Menu()
    try:
        menu.load_from_file("menu.json")
    except Exception as e:
        print(f"Nie udało się wczytać menu: {e}")

    customer_manager = CustomerManager()
    try:
        customer_manager.load_from_file("customers.json")
    except Exception as e:
        print(f"Nie udało się wczytać klientów: {e}")

    # Jeśli brak danych, tworzymy przykładowe
    if len(menu) == 0:
        print("\nTworzę przykładowe menu...")
        try:
            menu.add_pizza(Pizza("Margherita", 25.0))
            menu.add_pizza(Pizza("Pepperoni", 30.0))
            menu.add_pizza(Pizza("Hawajska", 32.0))
            menu.add_pizza(Pizza("Quattro Formaggi", 35.0))
        except InvalidPriceError as e:
            print(f"Błąd tworzenia pizzy: {e}")

    if len(customer_manager) == 0:
        print("\nTworzę przykładowych klientów...")
        customer_manager.add_customer(Customer("Jan Kowalski", "123-456-789"))
        customer_manager.add_customer(VIPCustomer("Anna Nowak", "987-654-321", 15))
        customer_manager.add_customer(VIPCustomer("Piotr Wiśniewski", "555-123-456", 20))

    # === WYŚWIETLANIE DANYCH ===
    menu.list_pizzas()
    customer_manager.list_customers()

    # === TWORZENIE ZAMÓWIEŃ ===
    print("\n--- Tworzenie zamówień ---")
    order_manager = OrderManager()

    # Zamówienie dla zwykłego klienta
    try:
        customer1 = customer_manager.find_customer(1)
        order1 = order_manager.create_order(customer1)

        pizza = menu.find_pizza("Margherita")
        order1.add_item(pizza, 2)

        pizza = menu.find_pizza("Pepperoni")
        order1.add_item(pizza, 1)

    except (CustomerNotFoundError, PizzaNotFoundError) as e:
        print(f"Błąd tworzenia zamówienia: {e}")

    # Zamówienie dla VIP klienta
    try:
        vip = customer_manager.find_customer(2)
        order2 = order_manager.create_order(vip)

        pizza = menu.find_pizza("Quattro Formaggi")
        order2.add_item(pizza, 2)

        # Dodaj punkty lojalnościowe
        if hasattr(vip, 'add_loyalty_points'):
            vip.add_loyalty_points(10)

    except (CustomerNotFoundError, PizzaNotFoundError) as e:
        print(f"Błąd tworzenia zamówienia: {e}")

    # === WYŚWIETLANIE ZAMÓWIEŃ ===
    print("\n--- Szczegóły zamówień ---")
    for order in order_manager:
        print()
        print(order)

    order_manager.list_orders()
    print(f"\nŁączny przychód: {order_manager.get_total_revenue():.2f} zł")

    # === DEMONSTRACJA OBSŁUGI BŁĘDÓW ===
    print("\n" + "=" * 60)
    print("DEMONSTRACJA OBSŁUGI WYJĄTKÓW")
    print("=" * 60)

    # Test 1: Nieprawidłowa cena
    print("\n1. Próba utworzenia pizzy z ujemną ceną:")
    try:
        invalid_pizza = Pizza("Test", -10)
    except InvalidPriceError as e:
        print(f"   Przechwycono: {e}")
        print(f"   Nieprawidłowa cena: {e.price}")

    # Test 2: Nieistniejąca pizza
    print("\n2. Próba znalezienia nieistniejącej pizzy:")
    try:
        menu.find_pizza("Carbonara")
    except PizzaNotFoundError as e:
        print(f"   Przechwycono: {e}")
        print(f"   Szukana pizza: {e.pizza_name}")

    # Test 3: Nieistniejący klient
    print("\n3. Próba znalezienia nieistniejącego klienta:")
    try:
        customer_manager.find_customer(999)
    except CustomerNotFoundError as e:
        print(f"   Przechwycono: {e}")
        print(f"   Szukane ID: {e.customer_id}")

    # Test 4: Puste zamówienie
    print("\n4. Próba przetworzenia pustego zamówienia:")
    try:
        empty_order = order_manager.create_order(customer1)
        empty_order.process()
    except EmptyOrderError as e:
        print(f"   Przechwycono: {e}")
        print(f"   ID zamówienia: {e.order_id}")

    # Test 5: Łapanie na poziomie bazowym
    print("\n5. Łapanie wszystkich błędów pizzerii:")
    errors_to_test = [
        lambda: Pizza("", 25),  # ValueError
        lambda: Pizza("Test", -5),  # InvalidPriceError
        lambda: menu.find_pizza("Nieistniejąca"),  # PizzaNotFoundError
    ]

    for i, error_func in enumerate(errors_to_test, 1):
        try:
            error_func()
        except PizzeriaError as e:
            print(f"   {i}. PizzeriaError: {type(e).__name__}: {e}")
        except ValueError as e:
            print(f"   {i}. ValueError: {e}")

    # === ZAPISYWANIE DANYCH ===
    print("\n" + "=" * 60)
    print("ZAPISYWANIE DANYCH")
    print("=" * 60)

    menu.save_to_file("menu.json")
    customer_manager.save_to_file("customers.json")

    print("\n" + "=" * 60)
    print("KONIEC PROGRAMU")
    print("=" * 60)
    print("\nDane zostały zapisane. Przy następnym uruchomieniu")
    print("zostaną wczytane automatycznie.")


if __name__ == "__main__":
    main()
