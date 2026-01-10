# Klasy Pizza i Menu z pełną obsługą wyjątków i I/O
# Przykład rozwiązania dla Weekendu 2

import json
from exceptions import InvalidPriceError, PizzaNotFoundError, DuplicatePizzaError


class Pizza:
    """Reprezentuje pojedynczą pizzę w menu."""

    def __init__(self, name, price):
        """
        Tworzy nową pizzę.

        Args:
            name: Nazwa pizzy (niepusty string)
            price: Cena pizzy (liczba > 0)

        Raises:
            ValueError: Jeśli nazwa pusta lub nie jest stringiem
            InvalidPriceError: Jeśli cena <= 0
        """
        # Walidacja nazwy
        if not name:
            raise ValueError("Nazwa pizzy nie może być pusta!")
        if not isinstance(name, str):
            raise TypeError("Nazwa pizzy musi być tekstem!")

        # Walidacja ceny
        if not isinstance(price, (int, float)):
            raise TypeError("Cena musi być liczbą!")
        if price <= 0:
            raise InvalidPriceError(price)

        self.name = name
        self.price = float(price)

    def __str__(self):
        return f"{self.name}: {self.price} zł"

    def __repr__(self):
        return f"Pizza(name='{self.name}', price={self.price})"

    def __eq__(self, other):
        if isinstance(other, Pizza):
            return self.name == other.name and self.price == other.price
        return False

    def update_price(self, new_price):
        """
        Aktualizuje cenę pizzy.

        Args:
            new_price: Nowa cena (> 0)

        Raises:
            InvalidPriceError: Jeśli nowa cena <= 0
        """
        if new_price <= 0:
            raise InvalidPriceError(new_price)
        self.price = float(new_price)

    def apply_discount(self, percent):
        """
        Oblicza cenę po rabacie.

        Args:
            percent: Procent rabatu (0-100)

        Returns:
            Cena po rabacie
        """
        if percent < 0 or percent > 100:
            raise ValueError("Rabat musi być w zakresie 0-100%")
        return self.price * (1 - percent / 100)

    def to_dict(self):
        """Konwertuje pizzę do słownika (serializacja)."""
        return {
            "name": self.name,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data):
        """Tworzy pizzę ze słownika (deserializacja)."""
        return cls(data["name"], data["price"])


class Menu:
    """Zarządza kolekcją pizz w menu."""

    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        """
        Dodaje pizzę do menu.

        Args:
            pizza: Obiekt Pizza do dodania

        Raises:
            TypeError: Jeśli pizza nie jest instancją Pizza
            DuplicatePizzaError: Jeśli pizza o tej nazwie już istnieje
        """
        if not isinstance(pizza, Pizza):
            raise TypeError("Oczekiwano obiektu Pizza!")

        # Sprawdź duplikaty
        for p in self.pizzas:
            if p.name == pizza.name:
                raise DuplicatePizzaError(pizza.name)

        self.pizzas.append(pizza)
        print(f"Dodano pizzę: {pizza}")

    def remove_pizza(self, name):
        """
        Usuwa pizzę z menu.

        Args:
            name: Nazwa pizzy do usunięcia

        Raises:
            PizzaNotFoundError: Jeśli pizza nie istnieje
        """
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                print(f"Usunięto pizzę: {name}")
                return

        raise PizzaNotFoundError(name)

    def find_pizza(self, name):
        """
        Znajduje pizzę po nazwie.

        Args:
            name: Nazwa pizzy

        Returns:
            Obiekt Pizza

        Raises:
            PizzaNotFoundError: Jeśli pizza nie istnieje
        """
        for pizza in self.pizzas:
            if pizza.name == name:
                return pizza

        raise PizzaNotFoundError(name)

    def list_pizzas(self):
        """Wyświetla wszystkie pizze w menu."""
        if not self.pizzas:
            print("Menu jest puste.")
            return

        print("\n=== MENU PIZZERII ===")
        for pizza in self.pizzas:
            print(f"  - {pizza}")
        print(f"Razem: {len(self.pizzas)} pizz")

    def get_cheapest(self):
        """Zwraca najtańszą pizzę lub None."""
        if not self.pizzas:
            return None
        return min(self.pizzas, key=lambda p: p.price)

    def get_most_expensive(self):
        """Zwraca najdroższą pizzę lub None."""
        if not self.pizzas:
            return None
        return max(self.pizzas, key=lambda p: p.price)

    def get_average_price(self):
        """Zwraca średnią cenę pizz."""
        if not self.pizzas:
            return 0.0
        return sum(p.price for p in self.pizzas) / len(self.pizzas)

    def __len__(self):
        return len(self.pizzas)

    def __iter__(self):
        return iter(self.pizzas)

    def __contains__(self, pizza):
        return pizza in self.pizzas

    # === Metody I/O ===

    def save_to_file(self, filename):
        """
        Zapisuje menu do pliku JSON.

        Args:
            filename: Ścieżka do pliku

        Raises:
            IOError: W przypadku błędu zapisu
        """
        try:
            data = [pizza.to_dict() for pizza in self.pizzas]
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Zapisano menu ({len(self.pizzas)} pizz) do {filename}")
        except IOError as e:
            print(f"Błąd zapisu do pliku: {e}")
            raise

    def load_from_file(self, filename):
        """
        Wczytuje menu z pliku JSON.

        Args:
            filename: Ścieżka do pliku

        Note:
            Jeśli plik nie istnieje, menu pozostaje puste.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.pizzas = [Pizza.from_dict(item) for item in data]
            print(f"Wczytano {len(self.pizzas)} pizz z {filename}")
        except FileNotFoundError:
            print(f"Plik {filename} nie istnieje - tworzę puste menu")
            self.pizzas = []
        except json.JSONDecodeError as e:
            print(f"Błąd parsowania JSON: {e}")
            self.pizzas = []


# === Demonstracja ===

if __name__ == "__main__":
    print("=== Demonstracja Pizza i Menu z wyjątkami ===\n")

    # Test tworzenia pizzy
    print("--- Tworzenie pizz ---")
    try:
        pizza1 = Pizza("Margherita", 25.0)
        print(f"Utworzono: {pizza1}")

        pizza_invalid = Pizza("Test", -10)
    except InvalidPriceError as e:
        print(f"Błąd: {e}")

    # Test menu
    print("\n--- Operacje na menu ---")
    menu = Menu()
    menu.add_pizza(Pizza("Margherita", 25.0))
    menu.add_pizza(Pizza("Pepperoni", 30.0))
    menu.add_pizza(Pizza("Hawajska", 32.0))

    menu.list_pizzas()

    # Test duplikatu
    print("\n--- Test duplikatu ---")
    try:
        menu.add_pizza(Pizza("Margherita", 28.0))
    except DuplicatePizzaError as e:
        print(f"Błąd: {e}")

    # Test wyszukiwania
    print("\n--- Test wyszukiwania ---")
    try:
        found = menu.find_pizza("Pepperoni")
        print(f"Znaleziono: {found}")

        not_found = menu.find_pizza("Carbonara")
    except PizzaNotFoundError as e:
        print(f"Błąd: {e}")

    # Test I/O
    print("\n--- Test zapisu/odczytu ---")
    menu.save_to_file("menu_demo.json")

    menu2 = Menu()
    menu2.load_from_file("menu_demo.json")
    menu2.list_pizzas()

    # Cleanup
    import os
    os.remove("menu_demo.json")
    print("\nUsunięto plik demo.")
