# Klasy Customer z pełną obsługą wyjątków i I/O
# Przykład rozwiązania dla Weekendu 2

import json
from exceptions import CustomerNotFoundError, InvalidDiscountError


class Customer:
    """Reprezentuje klienta pizzerii."""

    _next_id = 1

    def __init__(self, name, phone):
        """
        Tworzy nowego klienta.

        Args:
            name: Imię klienta (niepuste)
            phone: Numer telefonu

        Raises:
            ValueError: Jeśli nazwa pusta
        """
        if not name:
            raise ValueError("Nazwa klienta nie może być pusta!")
        if not isinstance(name, str):
            raise TypeError("Nazwa klienta musi być tekstem!")

        self.name = name
        self.phone = phone
        self.id = Customer._next_id
        Customer._next_id += 1

    def __str__(self):
        return f"Klient {self.id}: {self.name}, tel: {self.phone}"

    def __repr__(self):
        return f"Customer(name='{self.name}', phone='{self.phone}', id={self.id})"

    def update_phone(self, new_phone):
        """Aktualizuje numer telefonu."""
        self.phone = new_phone

    @classmethod
    def reset_id_counter(cls):
        """Resetuje licznik ID (przydatne w testach)."""
        cls._next_id = 1

    def to_dict(self):
        """Konwertuje klienta do słownika."""
        return {
            "type": "Customer",
            "id": self.id,
            "name": self.name,
            "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data):
        """Tworzy klienta ze słownika."""
        customer = cls(data["name"], data["phone"])
        customer.id = data["id"]
        return customer


class VIPCustomer(Customer):
    """Klient VIP z rabatem i punktami lojalnościowymi."""

    def __init__(self, name, phone, discount_percent=10):
        """
        Tworzy klienta VIP.

        Args:
            name: Imię klienta
            phone: Numer telefonu
            discount_percent: Procent rabatu (0-100)

        Raises:
            InvalidDiscountError: Jeśli rabat poza zakresem 0-100
        """
        super().__init__(name, phone)

        if not isinstance(discount_percent, (int, float)):
            raise TypeError("Rabat musi być liczbą!")
        if discount_percent < 0 or discount_percent > 100:
            raise InvalidDiscountError(discount_percent)

        self.discount_percent = discount_percent
        self.loyalty_points = 0

    def __str__(self):
        return f"VIP {super().__str__()}, zniżka: {self.discount_percent}%, punkty: {self.loyalty_points}"

    def add_loyalty_points(self, points):
        """
        Dodaje punkty lojalnościowe.

        Args:
            points: Liczba punktów do dodania (> 0)

        Raises:
            ValueError: Jeśli points <= 0
        """
        if points <= 0:
            raise ValueError("Liczba punktów musi być dodatnia!")
        self.loyalty_points += points

    def apply_discount(self, amount):
        """
        Stosuje rabat VIP do kwoty.

        Args:
            amount: Kwota przed rabatem

        Returns:
            Kwota po rabacie
        """
        return amount * (1 - self.discount_percent / 100)

    def to_dict(self):
        """Konwertuje VIP klienta do słownika."""
        data = super().to_dict()
        data["type"] = "VIPCustomer"
        data["discount_percent"] = self.discount_percent
        data["loyalty_points"] = self.loyalty_points
        return data

    @classmethod
    def from_dict(cls, data):
        """Tworzy VIP klienta ze słownika."""
        vip = cls(data["name"], data["phone"], data["discount_percent"])
        vip.id = data["id"]
        vip.loyalty_points = data.get("loyalty_points", 0)
        return vip


class CustomerManager:
    """Zarządza kolekcją klientów."""

    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        """
        Dodaje klienta.

        Args:
            customer: Obiekt Customer lub VIPCustomer

        Raises:
            TypeError: Jeśli nie jest instancją Customer
        """
        if not isinstance(customer, Customer):
            raise TypeError("Oczekiwano obiektu Customer lub jego podklasy!")
        self.customers.append(customer)
        print(f"Dodano: {customer}")

    def remove_customer(self, customer_id):
        """
        Usuwa klienta po ID.

        Raises:
            CustomerNotFoundError: Jeśli klient nie istnieje
        """
        for customer in self.customers:
            if customer.id == customer_id:
                self.customers.remove(customer)
                print(f"Usunięto klienta ID: {customer_id}")
                return

        raise CustomerNotFoundError(customer_id)

    def find_customer(self, customer_id):
        """
        Znajduje klienta po ID.

        Raises:
            CustomerNotFoundError: Jeśli klient nie istnieje
        """
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

        raise CustomerNotFoundError(customer_id)

    def list_customers(self):
        """Wyświetla wszystkich klientów."""
        if not self.customers:
            print("Brak klientów.")
            return

        print("\n=== LISTA KLIENTÓW ===")
        for customer in self.customers:
            print(f"  - {customer}")
        print(f"Razem: {len(self.customers)} klientów")

    def __len__(self):
        return len(self.customers)

    def __iter__(self):
        return iter(self.customers)

    # === Metody I/O ===

    def save_to_file(self, filename):
        """Zapisuje klientów do pliku JSON."""
        try:
            data = [customer.to_dict() for customer in self.customers]
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Zapisano {len(self.customers)} klientów do {filename}")
        except IOError as e:
            print(f"Błąd zapisu: {e}")
            raise

    def load_from_file(self, filename):
        """Wczytuje klientów z pliku JSON."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.customers = []
            for item in data:
                if item.get("type") == "VIPCustomer":
                    customer = VIPCustomer.from_dict(item)
                else:
                    customer = Customer.from_dict(item)
                self.customers.append(customer)

            # Aktualizuj licznik ID
            if self.customers:
                max_id = max(c.id for c in self.customers)
                Customer._next_id = max_id + 1

            print(f"Wczytano {len(self.customers)} klientów z {filename}")
        except FileNotFoundError:
            print(f"Plik {filename} nie istnieje")
            self.customers = []


# === Demonstracja ===

if __name__ == "__main__":
    print("=== Demonstracja Customer z wyjątkami ===\n")

    Customer.reset_id_counter()

    # Test tworzenia klientów
    print("--- Tworzenie klientów ---")
    customer1 = Customer("Jan Kowalski", "123-456-789")
    print(customer1)

    vip = VIPCustomer("Anna Nowak", "987-654-321", 15)
    print(vip)

    # Test nieprawidłowego rabatu
    print("\n--- Test walidacji rabatu ---")
    try:
        invalid_vip = VIPCustomer("Test", "000", 150)
    except InvalidDiscountError as e:
        print(f"Błąd: {e}")

    # Test CustomerManager
    print("\n--- Test CustomerManager ---")
    manager = CustomerManager()
    manager.add_customer(customer1)
    manager.add_customer(vip)
    manager.list_customers()

    # Test wyszukiwania
    print("\n--- Test wyszukiwania ---")
    try:
        found = manager.find_customer(1)
        print(f"Znaleziono: {found}")

        not_found = manager.find_customer(999)
    except CustomerNotFoundError as e:
        print(f"Błąd: {e}")

    # Test I/O
    print("\n--- Test zapisu/odczytu ---")
    manager.save_to_file("customers_demo.json")

    Customer.reset_id_counter()
    manager2 = CustomerManager()
    manager2.load_from_file("customers_demo.json")
    manager2.list_customers()

    # Cleanup
    import os
    os.remove("customers_demo.json")
    print("\nUsunięto plik demo.")
