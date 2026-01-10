# Klasy Order - reprezentują zamówienia
# Baza startowa dla Weekendu 2 (bez obsługi wyjątków - to będzie temat tego weekendu!)

from pizza import Pizza
from customer import Customer


class OrderItem:
    """Reprezentuje pojedynczą pozycję w zamówieniu."""

    def __init__(self, pizza, quantity):
        # TODO: Dodamy walidację z wyjątkami
        self.pizza = pizza
        self.quantity = quantity

    @property
    def total_price(self):
        """Oblicza łączną cenę pozycji."""
        return self.pizza.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} ({self.total_price} zł)"


class Order:
    """Reprezentuje zamówienie klienta."""

    _next_id = 1

    def __init__(self, customer):
        # TODO: Dodamy walidację typu customer z wyjątkiem
        self.customer = customer
        self.items = []
        self.id = Order._next_id
        Order._next_id += 1

    def add_item(self, pizza, quantity):
        """Dodaje pozycję do zamówienia."""
        item = OrderItem(pizza, quantity)
        self.items.append(item)
        print(f"Dodano do zamówienia: {item}")

    def remove_item(self, pizza_name):
        """Usuwa pozycję z zamówienia po nazwie pizzy."""
        for item in self.items:
            if item.pizza.name == pizza_name:
                self.items.remove(item)
                print(f"Usunięto z zamówienia: {pizza_name}")
                return True
        print(f"Nie znaleziono pozycji: {pizza_name}")
        return False

    @property
    def total_price(self):
        """Oblicza łączną cenę zamówienia."""
        total = sum(item.total_price for item in self.items)
        # Zastosuj zniżkę dla VIP
        if hasattr(self.customer, 'apply_discount'):
            total = self.customer.apply_discount(total)
        return total

    def __str__(self):
        items_str = "\n".join(f"  - {item}" for item in self.items)
        return f"Zamówienie ID: {self.id}\nKlient: {self.customer.name}\nPozycje:\n{items_str}\nŁącznie: {self.total_price} zł"

    def __len__(self):
        return len(self.items)

    @classmethod
    def reset_id_counter(cls):
        """Resetuje licznik ID (przydatne w testach)."""
        cls._next_id = 1


class OrderManager:
    """Zarządza kolekcją zamówień."""

    def __init__(self):
        self.orders = []

    def create_order(self, customer):
        """Tworzy nowe zamówienie dla klienta."""
        order = Order(customer)
        self.orders.append(order)
        print(f"Utworzono zamówienie #{order.id} dla {customer.name}")
        return order

    def cancel_order(self, order_id):
        """Anuluje zamówienie po ID."""
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                print(f"Anulowano zamówienie ID: {order_id}")
                return True
        print(f"Nie znaleziono zamówienia o ID {order_id}")
        return False

    def find_order(self, order_id):
        """Znajduje zamówienie po ID."""
        for order in self.orders:
            if order.id == order_id:
                return order
        # TODO: Zmienimy na rzucanie wyjątku zamiast zwracania None
        return None

    def list_orders(self):
        """Wyświetla wszystkie zamówienia."""
        if not self.orders:
            print("Brak zamówień.")
            return
        print("Wszystkie zamówienia:")
        for order in self.orders:
            print(f"  - ID: {order.id}, Klient: {order.customer.name}, Łącznie: {order.total_price} zł")

    def __len__(self):
        return len(self.orders)
