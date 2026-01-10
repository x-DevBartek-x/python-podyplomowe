# Klasy Order z pełną obsługą wyjątków
# Przykład rozwiązania dla Weekendu 2

import json
from pizza import Pizza
from customer import Customer
from exceptions import (
    InvalidQuantityError,
    OrderNotFoundError,
    EmptyOrderError
)


class OrderItem:
    """Reprezentuje pojedynczą pozycję w zamówieniu."""

    def __init__(self, pizza, quantity):
        """
        Tworzy pozycję zamówienia.

        Args:
            pizza: Obiekt Pizza
            quantity: Ilość (> 0)

        Raises:
            TypeError: Jeśli pizza nie jest instancją Pizza
            InvalidQuantityError: Jeśli quantity <= 0
        """
        if not isinstance(pizza, Pizza):
            raise TypeError("Oczekiwano obiektu Pizza!")
        if not isinstance(quantity, int):
            raise TypeError("Ilość musi być liczbą całkowitą!")
        if quantity <= 0:
            raise InvalidQuantityError(quantity)

        self.pizza = pizza
        self.quantity = quantity

    @property
    def total_price(self):
        """Oblicza łączną cenę pozycji."""
        return self.pizza.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} ({self.total_price} zł)"

    def to_dict(self):
        """Konwertuje do słownika."""
        return {
            "pizza": self.pizza.to_dict(),
            "quantity": self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        """Tworzy z słownika."""
        pizza = Pizza.from_dict(data["pizza"])
        return cls(pizza, data["quantity"])


class Order:
    """Reprezentuje zamówienie klienta."""

    _next_id = 1

    def __init__(self, customer):
        """
        Tworzy zamówienie.

        Args:
            customer: Obiekt Customer

        Raises:
            TypeError: Jeśli customer nie jest instancją Customer
        """
        if not isinstance(customer, Customer):
            raise TypeError("Oczekiwano obiektu Customer!")

        self.customer = customer
        self.items = []
        self.id = Order._next_id
        Order._next_id += 1

    def add_item(self, pizza, quantity):
        """
        Dodaje pozycję do zamówienia.

        Args:
            pizza: Obiekt Pizza
            quantity: Ilość

        Raises:
            InvalidQuantityError: Jeśli quantity <= 0
        """
        item = OrderItem(pizza, quantity)
        self.items.append(item)
        print(f"Dodano do zamówienia #{self.id}: {item}")

    def remove_item(self, pizza_name):
        """
        Usuwa pozycję z zamówienia.

        Args:
            pizza_name: Nazwa pizzy do usunięcia

        Returns:
            True jeśli usunięto, False jeśli nie znaleziono
        """
        for item in self.items:
            if item.pizza.name == pizza_name:
                self.items.remove(item)
                print(f"Usunięto z zamówienia #{self.id}: {pizza_name}")
                return True
        return False

    @property
    def total_price(self):
        """Oblicza łączną cenę zamówienia (z rabatem VIP)."""
        total = sum(item.total_price for item in self.items)

        # Zastosuj rabat dla VIP
        if hasattr(self.customer, 'apply_discount'):
            total = self.customer.apply_discount(total)

        return total

    def process(self):
        """
        Przetwarza zamówienie.

        Raises:
            EmptyOrderError: Jeśli zamówienie jest puste
        """
        if not self.items:
            raise EmptyOrderError(self.id)

        print(f"\nPrzetwarzanie zamówienia #{self.id}...")
        print(f"Klient: {self.customer.name}")
        print(f"Łączna kwota: {self.total_price} zł")
        print("Zamówienie przyjęte do realizacji!")

    def __str__(self):
        items_str = "\n".join(f"  - {item}" for item in self.items)
        discount_info = ""
        if hasattr(self.customer, 'discount_percent'):
            discount_info = f" (po rabacie VIP {self.customer.discount_percent}%)"

        return (f"Zamówienie #{self.id}\n"
                f"Klient: {self.customer.name}\n"
                f"Pozycje:\n{items_str}\n"
                f"Łącznie: {self.total_price} zł{discount_info}")

    def __len__(self):
        return len(self.items)

    @classmethod
    def reset_id_counter(cls):
        """Resetuje licznik ID."""
        cls._next_id = 1


class OrderManager:
    """Zarządza kolekcją zamówień."""

    def __init__(self):
        self.orders = []

    def create_order(self, customer):
        """
        Tworzy nowe zamówienie.

        Args:
            customer: Obiekt Customer

        Returns:
            Nowy obiekt Order
        """
        order = Order(customer)
        self.orders.append(order)
        print(f"Utworzono zamówienie #{order.id} dla {customer.name}")
        return order

    def cancel_order(self, order_id):
        """
        Anuluje zamówienie.

        Raises:
            OrderNotFoundError: Jeśli zamówienie nie istnieje
        """
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                print(f"Anulowano zamówienie #{order_id}")
                return

        raise OrderNotFoundError(order_id)

    def find_order(self, order_id):
        """
        Znajduje zamówienie po ID.

        Raises:
            OrderNotFoundError: Jeśli zamówienie nie istnieje
        """
        for order in self.orders:
            if order.id == order_id:
                return order

        raise OrderNotFoundError(order_id)

    def list_orders(self):
        """Wyświetla wszystkie zamówienia."""
        if not self.orders:
            print("Brak zamówień.")
            return

        print("\n=== WSZYSTKIE ZAMÓWIENIA ===")
        for order in self.orders:
            status = "puste" if len(order) == 0 else f"{len(order)} poz."
            print(f"  - #{order.id}: {order.customer.name} - {order.total_price} zł ({status})")

    def get_total_revenue(self):
        """Oblicza łączny przychód ze wszystkich zamówień."""
        return sum(order.total_price for order in self.orders)

    def __len__(self):
        return len(self.orders)

    def __iter__(self):
        return iter(self.orders)


# === Demonstracja ===

if __name__ == "__main__":
    from customer import Customer, VIPCustomer

    print("=== Demonstracja Order z wyjątkami ===\n")

    Customer.reset_id_counter()
    Order.reset_id_counter()

    # Przygotowanie
    customer = Customer("Jan Kowalski", "123")
    vip = VIPCustomer("Anna Nowak", "456", 20)

    pizza1 = Pizza("Margherita", 25.0)
    pizza2 = Pizza("Pepperoni", 30.0)

    # Test OrderManager
    print("--- Tworzenie zamówień ---")
    manager = OrderManager()

    order1 = manager.create_order(customer)
    order1.add_item(pizza1, 2)
    order1.add_item(pizza2, 1)

    order2 = manager.create_order(vip)
    order2.add_item(pizza1, 1)

    print("\n--- Szczegóły zamówień ---")
    print(order1)
    print()
    print(order2)

    # Test InvalidQuantityError
    print("\n--- Test walidacji ilości ---")
    try:
        order1.add_item(pizza1, -1)
    except InvalidQuantityError as e:
        print(f"Błąd: {e}")

    # Test EmptyOrderError
    print("\n--- Test pustego zamówienia ---")
    empty_order = manager.create_order(customer)
    try:
        empty_order.process()
    except EmptyOrderError as e:
        print(f"Błąd: {e}")

    # Test OrderNotFoundError
    print("\n--- Test wyszukiwania ---")
    try:
        manager.find_order(999)
    except OrderNotFoundError as e:
        print(f"Błąd: {e}")

    # Podsumowanie
    print("\n--- Podsumowanie ---")
    manager.list_orders()
    print(f"Łączny przychód: {manager.get_total_revenue()} zł")
