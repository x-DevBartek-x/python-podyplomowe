# Klasy Customer - reprezentują klientów pizzerii
# Baza startowa dla Weekendu 2 (bez obsługi wyjątków - to będzie temat tego weekendu!)

class Customer:
    """Reprezentuje klienta pizzerii."""

    _next_id = 1  # Klasowa zmienna do generowania ID

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.id = Customer._next_id
        Customer._next_id += 1

    def __str__(self):
        return f"Klient {self.id}: {self.name}, tel: {self.phone}"

    def __repr__(self):
        return f"Customer(name='{self.name}', phone='{self.phone}', id={self.id})"

    def update_phone(self, new_phone):
        """Aktualizuje numer telefonu klienta."""
        self.phone = new_phone

    @classmethod
    def reset_id_counter(cls):
        """Resetuje licznik ID (przydatne w testach)."""
        cls._next_id = 1


class VIPCustomer(Customer):
    """Klient VIP z rabatem i punktami lojalnościowymi."""

    def __init__(self, name, phone, discount_percent=10):
        super().__init__(name, phone)
        self.discount_percent = discount_percent
        self.loyalty_points = 0

    def __str__(self):
        return f"VIP {super().__str__()}, zniżka: {self.discount_percent}%, punkty: {self.loyalty_points}"

    def add_loyalty_points(self, points):
        """Dodaje punkty lojalnościowe."""
        # TODO: Dodamy walidację punktów z wyjątkiem
        self.loyalty_points += points

    def apply_discount(self, amount):
        """Stosuje rabat VIP do kwoty."""
        return amount * (1 - self.discount_percent / 100)


class CustomerManager:
    """Zarządza kolekcją klientów."""

    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        """Dodaje klienta do listy."""
        # TODO: Dodamy sprawdzenie typu z wyjątkiem
        self.customers.append(customer)
        print(f"Dodano {customer}")

    def remove_customer(self, customer_id):
        """Usuwa klienta po ID."""
        for customer in self.customers:
            if customer.id == customer_id:
                self.customers.remove(customer)
                print(f"Usunięto klienta ID: {customer_id}")
                return True
        print(f"Nie znaleziono klienta o ID {customer_id}")
        return False

    def find_customer(self, customer_id):
        """Znajduje klienta po ID."""
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        # TODO: Zmienimy na rzucanie wyjątku zamiast zwracania None
        return None

    def list_customers(self):
        """Wyświetla wszystkich klientów."""
        if not self.customers:
            print("Brak klientów.")
            return
        print("Lista klientów:")
        for customer in self.customers:
            print(f"  - {customer}")

    def __len__(self):
        return len(self.customers)
