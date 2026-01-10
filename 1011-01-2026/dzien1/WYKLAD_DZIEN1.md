# Wykład: Obsługa wyjątków i operacje I/O - Dzień 1

## Agenda

**Czas trwania:** 8:30 - 15:00 (6h 30min z przerwami)

### Harmonogram

| Czas | Temat | Aktywność |
|------|-------|-----------|
| **8:30 - 8:50** | Powitanie i recap Weekendu 1 | Przypomnienie OOP, Q&A |
| **8:50 - 9:20** | Teoria: Wyjątki w Pythonie | Wykład: try/except, raise |
| **9:20 - 9:50** | Live coding: Przechwytywanie wyjątków | Teoria + demo + ćwiczenie (10 min) |
| **9:50 - 10:30** | Live coding: Rzucanie wyjątków | Teoria + demo + ćwiczenie (15 min) |
| **10:30 - 10:40** | **PRZERWA** | 10 minut |
| **10:40 - 11:20** | Live coding: Własne wyjątki | Teoria + demo + ćwiczenie (15 min) |
| **11:20 - 12:00** | Live coding: Hierarchia wyjątków | Teoria + demo + ćwiczenie (15 min) |
| **12:00 - 12:40** | Praktyka: Refaktoryzacja pizzerii | Dodawanie wyjątków do naszej aplikacji |
| **12:40 - 13:10** | **PRZERWA** | 30 minut |
| **13:10 - 13:40** | Teoria: Operacje I/O | Wykład: pliki, context managers |
| **13:40 - 14:10** | Live coding: Praca z plikami | Teoria + demo + ćwiczenie (15 min) |
| **14:10 - 14:40** | Live coding: JSON i serializacja | Teoria + demo + ćwiczenie (15 min) |
| **14:40 - 14:55** | Integracja: Zapis/odczyt pizzerii | Dodanie persystencji do aplikacji |
| **14:55 - 15:00** | Podsumowanie | Recap + Q&A |

### Co zbudujemy dzisiaj?

Rozbudowa aplikacji pizzerii o:
- **Walidację danych** z własnymi wyjątkami
- **Obsługę błędów** - eleganckie reagowanie na problemy
- **Persystencję** - zapis i odczyt danych do plików JSON

### Czego się nauczysz?

- Przechwytywanie wyjątków (try/except/finally)
- Rzucanie wyjątków (raise)
- Definiowanie własnych klas wyjątków
- Hierarchia wyjątków i ich dziedziczenie
- Operacje na plikach (open, read, write)
- Context managers (with statement)
- Serializacja obiektów do JSON

### Przygotowanie

Upewnij się, że masz:
- Kod z Weekendu 1 (lub użyj `baza_startowa/`)
- Python 3.8+ zainstalowany
- Edytor kodu gotowy do pracy

---

## Część 1: Wprowadzenie do wyjątków

### Teoria: Co to są wyjątki?

**Wyjątek** to sygnał, że podczas wykonywania programu wystąpił błąd lub nietypowa sytuacja.

```python
# Przykłady typowych wyjątków:
print(10 / 0)           # ZeroDivisionError
print(int("abc"))       # ValueError
print(my_list[100])     # IndexError
print(my_dict["key"])   # KeyError
```

**Bez obsługi wyjątków** program się zatrzymuje i wyświetla traceback:

```
Traceback (most recent call last):
  File "example.py", line 1, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```

### Hierarchia wyjątków w Pythonie

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ValueError
      ├── TypeError
      ├── KeyError
      ├── IndexError
      ├── FileNotFoundError
      ├── AttributeError
      └── ... (wiele innych)
```

**Kluczowe:**
- Wszystkie "normalne" wyjątki dziedziczą po `Exception`
- `SystemExit` i `KeyboardInterrupt` NIE dziedziczą po `Exception`
- Dzięki temu `except Exception:` nie łapie Ctrl+C

---

## Część 2: Przechwytywanie wyjątków (try/except)

### Teoria: Składnia try/except

```python
try:
    # Kod który może rzucić wyjątek
    result = 10 / number
except ZeroDivisionError:
    # Obsługa konkretnego wyjątku
    print("Nie można dzielić przez zero!")
```

### Pełna składnia

```python
try:
    # Kod ryzykowny
    result = some_operation()
except ValueError as e:
    # Obsługa ValueError, e to obiekt wyjątku
    print(f"Błąd wartości: {e}")
except (TypeError, KeyError) as e:
    # Obsługa wielu typów wyjątków
    print(f"Błąd typu lub klucza: {e}")
except Exception as e:
    # Obsługa wszystkich innych wyjątków
    print(f"Nieznany błąd: {e}")
else:
    # Wykonane TYLKO jeśli nie było wyjątku
    print("Operacja udana!")
finally:
    # Wykonane ZAWSZE (nawet po wyjątku)
    print("Sprzątanie...")
```

### Przykład praktyczny

```python
def safe_divide(a, b):
    """Bezpieczne dzielenie z obsługą błędów."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Błąd: Nie można dzielić przez zero!")
        return None
    except TypeError:
        print("Błąd: Argumenty muszą być liczbami!")
        return None
    else:
        print(f"Wynik: {result}")
        return result
    finally:
        print("Operacja dzielenia zakończona.")

# Testy
safe_divide(10, 2)   # Wynik: 5.0
safe_divide(10, 0)   # Błąd: dzielenie przez zero
safe_divide("a", 2)  # Błąd: argumenty muszą być liczbami
```

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

Stwórz plik `safe_operations.py` z funkcjami:

1. `safe_get_dict_value(slownik, klucz)`:
   - Pobiera wartość ze słownika
   - Obsługuje `KeyError` gdy klucz nie istnieje
   - Zwraca `None` w przypadku błędu

2. `safe_convert_to_int(value)`:
   - Próbuje przekonwertować wartość na int
   - Obsługuje `ValueError` gdy konwersja niemożliwa
   - Obsługuje `TypeError` gdy typ nieodpowiedni
   - Zwraca `None` w przypadku błędu

3. Przetestuj obie funkcje:
   ```python
   # Test słownika
   data = {"name": "Jan", "age": 25}
   print(safe_get_dict_value(data, "name"))     # Jan
   print(safe_get_dict_value(data, "missing"))  # None (KeyError)

   # Test konwersji
   print(safe_convert_to_int("42"))      # 42
   print(safe_convert_to_int("abc"))     # None (ValueError)
   print(safe_convert_to_int([1, 2]))    # None (TypeError)
   ```

**Oczekiwany output:**
```
Jan
Błąd: Klucz nie istnieje!
None
42
Błąd: Nie można przekonwertować na liczbę!
None
Błąd: Nieprawidłowy typ danych!
None
```

---

## Część 3: Rzucanie wyjątków (raise)

### Teoria: Kiedy rzucać wyjątki?

Wyjątki rzucamy gdy:
- Otrzymujemy nieprawidłowe dane wejściowe
- Obiekt jest w nieprawidłowym stanie
- Operacja nie może być wykonana
- Zasób nie istnieje

```python
def set_age(age):
    """Ustawia wiek z walidacją."""
    if not isinstance(age, int):
        raise TypeError("Wiek musi być liczbą całkowitą!")
    if age < 0:
        raise ValueError("Wiek nie może być ujemny!")
    if age > 150:
        raise ValueError("Wiek musi być realistyczny!")
    return age
```

### Składnia raise

```python
# Rzucenie wyjątku z komunikatem
raise ValueError("Nieprawidłowa wartość!")

# Rzucenie bez komunikatu
raise ValueError()

# Re-raise (ponowne rzucenie przechwyconego wyjątku)
try:
    something()
except ValueError:
    print("Loguję błąd...")
    raise  # Rzuca ponownie ten sam wyjątek
```

### Więcej przykładów walidacji

```python
def validate_email(email):
    """Waliduje format email."""
    if not isinstance(email, str):
        raise TypeError("Email musi być tekstem!")
    if "@" not in email:
        raise ValueError("Email musi zawierać @!")
    if not email.endswith((".pl", ".com", ".org")):
        raise ValueError("Nieprawidłowa domena email!")
    return email


def create_user(name, age, email):
    """Tworzy użytkownika z pełną walidacją."""
    # Walidacja nazwy
    if not name or not isinstance(name, str):
        raise ValueError("Nazwa musi być niepustym tekstem!")

    # Walidacja wieku (używamy set_age)
    validated_age = set_age(age)

    # Walidacja email
    validated_email = validate_email(email)

    return {"name": name, "age": validated_age, "email": validated_email}
```

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

Teraz zastosuj poznane techniki do klas pizzerii!

1. Zmodyfikuj klasę `Pizza` w `baza_startowa/pizza.py`:
   - Dodaj walidację w `__init__`:
     - Nazwa nie może być pusta (ValueError)
     - Nazwa musi być stringiem (TypeError)
     - Cena musi być > 0 (ValueError)
   - Dodaj walidację w `update_price`:
     - Nowa cena musi być > 0 (ValueError)

2. Zmodyfikuj klasę `VIPCustomer` w `baza_startowa/customer.py`:
   - `discount_percent` musi być w zakresie 0-100 (ValueError)
   - `add_loyalty_points` - points musi być > 0 (ValueError)

3. Przetestuj w interpreterze:
   ```python
   from pizza import Pizza
   from customer import VIPCustomer

   # Test Pizza
   try:
       pizza = Pizza("", 25.0)  # Pusta nazwa
   except ValueError as e:
       print(f"Błąd: {e}")

   try:
       pizza = Pizza("Margherita", -10)  # Ujemna cena
   except ValueError as e:
       print(f"Błąd: {e}")

   # Test VIPCustomer
   try:
       vip = VIPCustomer("Jan", "123", 150)  # Rabat > 100
   except ValueError as e:
       print(f"Błąd: {e}")
   ```

---

## Część 4: Własne wyjątki

### Teoria: Po co własne wyjątki?

**Standardowe wyjątki** (ValueError, TypeError) są ogólne.
**Własne wyjątki** pozwalają na:
- Precyzyjne określenie rodzaju błędu
- Łatwiejsze debugowanie
- Lepszą obsługę w kodzie wywołującym
- Grupowanie powiązanych błędów

### Definiowanie własnego wyjątku (przykład: sklep e-commerce)

```python
# Generyczny przykład - aplikacja e-commerce

class ShopError(Exception):
    """Bazowy wyjątek dla sklepu."""
    pass


class InvalidAmountError(ShopError):
    """Wyjątek dla nieprawidłowej kwoty."""

    def __init__(self, amount, message=None):
        self.amount = amount  # Przechowujemy kontekst błędu
        if message is None:
            message = f"Nieprawidłowa kwota: {amount} (musi być > 0)"
        super().__init__(message)


class ProductNotFoundError(ShopError):
    """Wyjątek gdy produkt nie istnieje."""

    def __init__(self, product_id):
        self.product_id = product_id
        super().__init__(f"Produkt o ID {product_id} nie został znaleziony")
```

### Użycie własnych wyjątków

```python
class Product:
    def __init__(self, name, price):
        if price <= 0:
            raise InvalidAmountError(price)
        self.name = name
        self.price = price


class Catalog:
    def find_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        raise ProductNotFoundError(product_id)
```

### Obsługa własnych wyjątków

```python
try:
    product = catalog.find_product(999)
except ProductNotFoundError as e:
    print(f"Nie znaleziono: {e.product_id}")
except ShopError as e:
    # Złapie wszystkie błędy sklepu
    print(f"Błąd aplikacji: {e}")
```

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

Teraz stwórz własne wyjątki dla aplikacji pizzerii!

1. Utwórz plik `exceptions.py` z hierarchią wyjątków:
   ```
   PizzeriaError (bazowy)
   ├── ValidationError
   │   ├── InvalidPriceError (atrybut: price)
   │   └── InvalidQuantityError (atrybut: quantity)
   └── NotFoundError
       ├── PizzaNotFoundError (atrybut: pizza_name)
       ├── CustomerNotFoundError (atrybut: customer_id)
       └── OrderNotFoundError (atrybut: order_id)
   ```

2. Każdy wyjątek powinien:
   - Dziedziczyć po odpowiednim rodzicu
   - Przyjmować specyficzne parametry
   - Mieć sensowny komunikat błędu

3. Przetestuj:
   ```python
   from exceptions import InvalidPriceError, CustomerNotFoundError

   raise InvalidPriceError(-10)
   # Output: InvalidPriceError: Nieprawidłowa cena: -10

   raise PizzaNotFoundError("Hawajska")
   # Output: PizzaNotFoundError: Pizza 'Hawajska' nie została znaleziona w menu
   ```

---

## Część 5: Hierarchia wyjątków w praktyce

### Teoria: Projektowanie hierarchii

```python
# exceptions.py

class PizzeriaError(Exception):
    """Bazowy wyjątek dla wszystkich błędów pizzerii."""
    pass


# === Błędy walidacji ===
class ValidationError(PizzeriaError):
    """Błędy związane z walidacją danych."""
    pass


class InvalidPriceError(ValidationError):
    """Nieprawidłowa cena."""
    def __init__(self, price):
        self.price = price
        super().__init__(f"Nieprawidłowa cena: {price}")


class InvalidQuantityError(ValidationError):
    """Nieprawidłowa ilość."""
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"Nieprawidłowa ilość: {quantity}")


# === Błędy wyszukiwania ===
class NotFoundError(PizzeriaError):
    """Błędy gdy element nie został znaleziony."""
    pass


class PizzaNotFoundError(NotFoundError):
    """Pizza nie została znaleziona."""
    def __init__(self, name):
        self.name = name
        super().__init__(f"Pizza '{name}' nie znaleziona")


class CustomerNotFoundError(NotFoundError):
    """Klient nie został znaleziony."""
    def __init__(self, customer_id):
        self.customer_id = customer_id
        super().__init__(f"Klient ID {customer_id} nie znaleziony")


class OrderNotFoundError(NotFoundError):
    """Zamówienie nie zostało znalezione."""
    def __init__(self, order_id):
        self.order_id = order_id
        super().__init__(f"Zamówienie ID {order_id} nie znalezione")
```

### Zalety hierarchii

```python
# Możemy łapać na różnych poziomach:

try:
    menu.find_pizza("Test")
except PizzaNotFoundError:
    # Tylko błędy pizzy
    pass
except NotFoundError:
    # Wszystkie błędy "nie znaleziono"
    pass
except ValidationError:
    # Wszystkie błędy walidacji
    pass
except PizzeriaError:
    # Wszystkie błędy aplikacji
    pass
```

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

1. Rozbuduj `exceptions.py` o pełną hierarchię (jak powyżej)

2. Zintegruj wyjątki z klasami:
   - `Pizza.__init__` → `InvalidPriceError`
   - `Menu.find_pizza` → `PizzaNotFoundError`
   - `CustomerManager.find_customer` → `CustomerNotFoundError`
   - `OrderManager.find_order` → `OrderNotFoundError`

3. W `main.py` dodaj blok demonstracyjny:
   ```python
   print("\n--- Demonstracja obsługi wyjątków ---")

   try:
       pizza = Pizza("Test", -10)
   except InvalidPriceError as e:
       print(f"Przechwycono: {e}")

   try:
       menu.find_pizza("Nieistniejąca")
   except PizzaNotFoundError as e:
       print(f"Przechwycono: {e}")
   ```

---

## Część 6: Refaktoryzacja pizzerii - wyjątki

### Zadanie zbiorcze (40 min)

Teraz połączymy wszystko w pełną refaktoryzację. Zmodyfikuj pliki:

**1. `exceptions.py`** - pełna hierarchia wyjątków

**2. `pizza.py`** - walidacja z wyjątkami:
```python
from exceptions import InvalidPriceError, PizzaNotFoundError

class Pizza:
    def __init__(self, name, price):
        if not name or not isinstance(name, str):
            raise ValueError("Nazwa pizzy musi być niepustym tekstem!")
        if price <= 0:
            raise InvalidPriceError(price)
        self.name = name
        self.price = price

    def update_price(self, new_price):
        if new_price <= 0:
            raise InvalidPriceError(new_price)
        self.price = new_price


class Menu:
    def find_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                return pizza
        raise PizzaNotFoundError(name)

    def add_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Oczekiwano obiektu Pizza!")
        # Sprawdź duplikaty
        for p in self.pizzas:
            if p.name == pizza.name:
                raise ValueError(f"Pizza '{pizza.name}' już istnieje w menu!")
        self.pizzas.append(pizza)
```

**3. `customer.py`** - analogiczne zmiany

**4. `order.py`** - analogiczne zmiany

**5. `main.py`** - demonstracja działania

---

## Część 7: Operacje wejścia/wyjścia (I/O)

### Teoria: Praca z plikami

```python
# Otwieranie pliku - sposób tradycyjny
file = open("data.txt", "r")
content = file.read()
file.close()  # WAŻNE: Zawsze zamykaj pliki!

# Otwieranie pliku - z context manager (ZALECANE)
with open("data.txt", "r") as file:
    content = file.read()
# Plik zamyka się automatycznie!
```

### Tryby otwierania plików

| Tryb | Opis |
|------|------|
| `"r"` | Odczyt (domyślny) |
| `"w"` | Zapis (nadpisuje!) |
| `"a"` | Dopisywanie |
| `"x"` | Tworzenie (błąd jeśli istnieje) |
| `"rb"` | Odczyt binarny |
| `"wb"` | Zapis binarny |

### Podstawowe operacje

```python
# ODCZYT
with open("data.txt", "r", encoding="utf-8") as f:
    # Cały plik jako string
    content = f.read()

    # Linia po linii
    for line in f:
        print(line.strip())

    # Wszystkie linie jako lista
    lines = f.readlines()

# ZAPIS
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Pierwsza linia\n")
    f.write("Druga linia\n")

    # Lub wiele linii naraz
    lines = ["Linia 1\n", "Linia 2\n", "Linia 3\n"]
    f.writelines(lines)

# DOPISYWANIE
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nowy wpis w logu\n")
```

### Obsługa błędów I/O

```python
try:
    with open("nieistniejacy.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Plik nie istnieje!")
except PermissionError:
    print("Brak uprawnień do pliku!")
except IOError as e:
    print(f"Błąd I/O: {e}")
```

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

Rozbuduj plik `io_demo.py` o funkcje JSON:

1. `save_dict_to_json(filename, data)`:
   - Zapisuje słownik do pliku JSON
   - Obsługuje błędy I/O
   - Zwraca True/False

2. `load_dict_from_json(filename)`:
   - Wczytuje słownik z pliku JSON
   - Obsługuje FileNotFoundError
   - Zwraca pusty słownik jeśli plik nie istnieje

3. Przetestuj:
   ```python
   data = {"menu": ["Margherita", "Pepperoni"], "count": 2}
   save_dict_to_json("menu.json", data)

   loaded = load_dict_from_json("menu.json")
   print(loaded)  # {'menu': ['Margherita', 'Pepperoni'], 'count': 2}

   # Test nieistniejącego pliku
   empty = load_dict_from_json("nieistniejacy.json")
   print(empty)  # {}
   ```

---

## Część 8: JSON i serializacja

### Teoria: Czym jest JSON?

**JSON** (JavaScript Object Notation) to popularny format wymiany danych.

```json
{
    "name": "Margherita",
    "price": 25.0,
    "ingredients": ["ser", "pomidory", "bazylia"]
}
```

**Mapowanie Python ↔ JSON:**
| Python | JSON |
|--------|------|
| dict | object {} |
| list | array [] |
| str | string "" |
| int, float | number |
| True/False | true/false |
| None | null |

### Moduł json

```python
import json

# Python → JSON (serializacja)
data = {"name": "Margherita", "price": 25.0}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Margherita", "price": 25.0}'

# JSON → Python (deserializacja)
json_string = '{"name": "Pepperoni", "price": 30.0}'
data = json.loads(json_string)
print(data["name"])  # Pepperoni

# Zapis do pliku
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Odczyt z pliku
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

### Serializacja obiektów

Obiekty Pythona nie są bezpośrednio serializowalne. Potrzebujemy metod pomocniczych:

```python
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

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


# Użycie
pizza = Pizza("Margherita", 25.0)
data = pizza.to_dict()
json_string = json.dumps(data)

# Odtworzenie
data = json.loads(json_string)
pizza_copy = Pizza.from_dict(data)
```

### Ćwiczenie praktyczne (10 min)

**Zadanie:**

Dodaj serializację do klas Customer i CustomerManager:

1. `Customer.to_dict()` i `Customer.from_dict(data)`:
   - Uwzględnij pole `"type": "Customer"` lub `"type": "VIPCustomer"`
   - VIPCustomer dodatkowo: `discount_percent`, `loyalty_points`

2. `CustomerManager.save_to_file(filename)` i `load_from_file(filename)`:
   - Przy wczytywaniu rozpoznaj typ (Customer vs VIPCustomer)

3. Przetestuj:
   ```python
   from customer import Customer, VIPCustomer, CustomerManager

   manager = CustomerManager()
   manager.add_customer(Customer("Jan", "123-456"))
   manager.add_customer(VIPCustomer("Anna", "789-000", 15))
   manager.save_to_file("customers.json")

   manager2 = CustomerManager()
   manager2.load_from_file("customers.json")
   manager2.list_customers()
   ```

**Zawartość `customers.json`:**
```json
[
  {"type": "Customer", "id": 1, "name": "Jan", "phone": "123-456"},
  {"type": "VIPCustomer", "id": 2, "name": "Anna", "phone": "789-000",
   "discount_percent": 15, "loyalty_points": 0}
]
```

---

## Część 9: Integracja - Persystencja danych

### Zadanie zbiorcze (15 min)

Dodaj persystencję do całej aplikacji pizzerii:

**1. Rozbuduj `Pizza` o serializację:**
```python
def to_dict(self):
    return {"name": self.name, "price": self.price}

@classmethod
def from_dict(cls, data):
    return cls(data["name"], data["price"])
```

**2. Rozbuduj `Customer` i `VIPCustomer`:**
```python
class Customer:
    def to_dict(self):
        return {
            "type": "Customer",
            "id": self.id,
            "name": self.name,
            "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data):
        customer = cls(data["name"], data["phone"])
        customer.id = data["id"]
        return customer


class VIPCustomer(Customer):
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "VIPCustomer"
        data["discount_percent"] = self.discount_percent
        data["loyalty_points"] = self.loyalty_points
        return data
```

**3. Rozbuduj `Menu` o zapis/odczyt:**
```python
import json

class Menu:
    def save_to_file(self, filename):
        data = [pizza.to_dict() for pizza in self.pizzas]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Zapisano menu do {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.pizzas = [Pizza.from_dict(item) for item in data]
            print(f"Wczytano {len(self.pizzas)} pizz z {filename}")
        except FileNotFoundError:
            print(f"Plik {filename} nie istnieje, tworzę puste menu.")
            self.pizzas = []
```

**4. Przetestuj w `main.py`:**
```python
# Zapis
menu.save_to_file("menu.json")
customer_manager.save_to_file("customers.json")

# Odczyt (nowa sesja)
menu2 = Menu()
menu2.load_from_file("menu.json")
menu2.list_pizzas()
```

---

## Część 10: Podsumowanie

### Co osiągnęliśmy?

**Obsługa wyjątków:**
- Przechwytywanie (try/except/finally)
- Rzucanie (raise)
- Własne klasy wyjątków
- Hierarchia wyjątków

**Operacje I/O:**
- Praca z plikami tekstowymi
- Context managers (with)
- Serializacja JSON
- Persystencja danych

### Porównanie: Przed i po

| Aspekt | Przed (Weekend 1) | Po (Weekend 2) |
|--------|------------------|----------------|
| **Walidacja** | Brak | Własne wyjątki |
| **Błędy** | Crash programu | Elegancka obsługa |
| **Persystencja** | Brak | JSON save/load |
| **Debugowanie** | Trudne | Łatwe (precyzyjne wyjątki) |

### Co jutro?

**Dzień 2 - Testowanie i debugowanie:**
- Testy jednostkowe z pytest
- Debugowanie z pdb i PyCharm
- Testy integracyjne i E2E

### Zadanie domowe (opcjonalne)

Rozbuduj aplikację o:
1. Zapis zamówień do pliku JSON
2. Wyjątek `DuplicatePizzaError` dla duplikatów w menu
3. Automatyczne wczytywanie danych przy starcie aplikacji

---

## Gratulacje!

Ukończyłeś Dzień 1 Weekendu 2!

Teraz Twoja aplikacja:
- Waliduje dane wejściowe
- Elegancko obsługuje błędy
- Zapisuje i wczytuje dane z plików

**Jutro dodamy testy i nauczymy się debugowania!**
