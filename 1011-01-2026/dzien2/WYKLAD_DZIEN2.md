# Wykład: Testowanie i debugowanie - Dzień 2

## Agenda

**Czas trwania:** 8:30 - 15:00 (6h 30min z przerwami)

### Harmonogram

| Czas | Temat | Aktywność |
|------|-------|-----------|
| **8:30 - 8:50** | Powitanie i recap Dnia 1 | Przypomnienie wyjątków i I/O |
| **8:50 - 9:20** | Teoria: Testowanie oprogramowania | Rodzaje testów, piramida testów |
| **9:20 - 9:50** | Live coding: Pierwszy test z pytest | Teoria + demo + ćwiczenie (10 min) |
| **9:50 - 10:30** | Live coding: Testowanie z asercjami | Teoria + demo + ćwiczenie (15 min) |
| **10:30 - 10:40** | **PRZERWA** | 10 minut |
| **10:40 - 11:10** | Live coding: Testowanie wyjątków | Teoria + demo + ćwiczenie (10 min) |
| **11:10 - 11:50** | Live coding: Fixtures i organizacja testów | Teoria + demo + ćwiczenie (15 min) |
| **11:50 - 12:40** | Praktyka: Testy dla pizzerii | Pisanie pełnego zestawu testów |
| **12:40 - 13:10** | **PRZERWA** | 30 minut |
| **13:10 - 13:40** | Teoria: Debugowanie | pdb, breakpoints, PyCharm |
| **13:40 - 14:10** | Live coding: Debugowanie z pdb | Teoria + demo + ćwiczenie (10 min) |
| **14:10 - 14:40** | Live coding: Debugowanie w PyCharm | Teoria + demo + ćwiczenie (10 min) |
| **14:40 - 14:55** | Testy integracyjne i E2E | Teoria + praktyka |
| **14:55 - 15:00** | Podsumowanie kursu | Recap + Q&A |

### Co zbudujemy dzisiaj?

- **Pełny zestaw testów** dla aplikacji pizzerii
- **Umiejętność debugowania** kodu krok po kroku
- **Testy różnych poziomów** (jednostkowe, integracyjne, E2E)

### Czego się nauczysz?

- Pisanie testów z pytest
- Asercje i sprawdzanie wyjątków
- Fixtures - przygotowanie danych testowych
- Debugowanie z pdb
- Debugowanie w PyCharm/VS Code
- Różnice między testami jednostkowymi, integracyjnymi i E2E

### Przygotowanie

```bash
# Instalacja pytest
pip install pytest

# Sprawdzenie instalacji
pytest --version
```

---

## Część 1: Wprowadzenie do testowania

### Teoria: Po co testować?

**Testy pozwalają:**
- Wykryć błędy PRZED wdrożeniem
- Ułatwiają refaktoryzację (pewność że nic nie zepsułeś)
- Dokumentują oczekiwane zachowanie kodu
- Oszczędzają czas w długiej perspektywie

**Bez testów:**
- "Działa na moim komputerze"
- Strach przed zmianami
- Ręczne testowanie każdej funkcji
- Błędy w produkcji

### Piramida testów

```
        /\
       /E2E\          <- Mało (wolne, drogie)
      /------\
     /Integracyjne\   <- Średnio
    /--------------\
   /  Jednostkowe   \ <- Dużo (szybkie, tanie)
  /------------------\
```

**Testy jednostkowe (Unit Tests):**
- Testują pojedyncze funkcje/metody
- Szybkie, izolowane
- Stanowią podstawę

**Testy integracyjne (Integration Tests):**
- Testują współpracę komponentów
- Np. Menu + Pizza razem

**Testy E2E (End-to-End):**
- Testują całą aplikację
- Symulują użytkownika
- Wolne, ale kompletne

### Konwencje nazewnictwa

```
projekt/
├── pizza.py           # Kod produkcyjny
├── customer.py
├── order.py
└── tests/             # Testy w osobnym katalogu
    ├── __init__.py
    ├── test_pizza.py   # Nazwa: test_<nazwa_modułu>.py
    ├── test_customer.py
    └── test_order.py
```

---

## Część 2: Pierwsze kroki z pytest

### Teoria: Struktura testu

```python
# test_example.py

def test_addition():
    """Testuje dodawanie dwóch liczb."""
    # Arrange (Przygotuj)
    a = 2
    b = 3

    # Act (Wykonaj)
    result = a + b

    # Assert (Sprawdź)
    assert result == 5
```

**Wzorzec AAA:**
- **Arrange** - przygotuj dane
- **Act** - wykonaj akcję
- **Assert** - sprawdź wynik

### Uruchamianie testów

```bash
# Wszystkie testy w bieżącym katalogu
pytest

# Konkretny plik
pytest test_pizza.py

# Konkretna funkcja
pytest test_pizza.py::test_pizza_creation

# Z większą szczegółowością
pytest -v

# Pokazuj print() podczas testów
pytest -s

# Zatrzymaj przy pierwszym błędzie
pytest -x
```

### Przykład: Test klasy Pizza

```python
# test_pizza.py
from pizza import Pizza


def test_pizza_creation():
    """Test tworzenia pizzy z poprawnymi danymi."""
    # Arrange & Act
    pizza = Pizza("Margherita", 25.0)

    # Assert
    assert pizza.name == "Margherita"
    assert pizza.price == 25.0


def test_pizza_str():
    """Test reprezentacji tekstowej pizzy."""
    pizza = Pizza("Pepperoni", 30.0)

    result = str(pizza)

    assert result == "Pepperoni: 30.0 zł"
```

### Ćwiczenie praktyczne (10 min)

**Zadanie:**

1. Utwórz plik `tests/test_pizza.py`

2. Napisz 3 testy:
   - `test_pizza_creation` - sprawdź że pizza ma poprawną nazwę i cenę
   - `test_pizza_equality` - sprawdź że dwie identyczne pizze są równe
   - `test_pizza_repr` - sprawdź reprezentację `repr()`

3. Uruchom testy:
   ```bash
   pytest tests/test_pizza.py -v
   ```

**Oczekiwany output:**
```
test_pizza.py::test_pizza_creation PASSED
test_pizza.py::test_pizza_equality PASSED
test_pizza.py::test_pizza_repr PASSED
```

---

## Część 3: Asercje w pytest

### Teoria: Rodzaje asercji

```python
# Równość
assert result == expected
assert result != unexpected

# Prawda/Fałsz
assert condition
assert not condition
assert result is True
assert result is False

# Tożsamość
assert obj1 is obj2
assert obj1 is not obj2

# Zawieranie
assert item in collection
assert item not in collection
assert "substr" in string

# Porównania
assert value > 0
assert value >= 0
assert value < 100

# Typ
assert isinstance(obj, Pizza)

# None
assert result is None
assert result is not None
```

### Asercje z komunikatami

```python
def test_pizza_price():
    pizza = Pizza("Test", 25.0)

    # Dodaj komunikat dla lepszego debugowania
    assert pizza.price > 0, f"Cena powinna być dodatnia, otrzymano: {pizza.price}"
```

### Przykład: Testy Menu

```python
# test_pizza.py
from pizza import Pizza, Menu


def test_menu_add_pizza():
    """Test dodawania pizzy do menu."""
    menu = Menu()
    pizza = Pizza("Margherita", 25.0)

    menu.add_pizza(pizza)

    assert len(menu) == 1
    assert pizza in menu.pizzas


def test_menu_find_pizza():
    """Test wyszukiwania pizzy."""
    menu = Menu()
    pizza = Pizza("Margherita", 25.0)
    menu.add_pizza(pizza)

    found = menu.find_pizza("Margherita")

    assert found is not None
    assert found.name == "Margherita"


def test_menu_find_pizza_not_exists():
    """Test wyszukiwania nieistniejącej pizzy."""
    menu = Menu()

    found = menu.find_pizza("Nieistniejąca")

    # Po refaktoryzacji to będzie rzucać wyjątek!
    assert found is None
```

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

1. Rozbuduj `test_pizza.py` o testy dla Menu:
   - `test_menu_empty` - nowe menu jest puste
   - `test_menu_add_pizza` - dodanie pizzy zwiększa rozmiar
   - `test_menu_add_multiple` - można dodać wiele pizz
   - `test_menu_find_existing` - znajdź istniejącą pizzę
   - `test_menu_len` - `len(menu)` zwraca poprawną wartość

2. Uruchom wszystkie testy:
   ```bash
   pytest tests/ -v
   ```

---

## Część 4: Testowanie wyjątków

### Teoria: pytest.raises

```python
import pytest
from pizza import Pizza
from exceptions import InvalidPriceError


def test_pizza_negative_price():
    """Test że ujemna cena rzuca wyjątek."""
    with pytest.raises(InvalidPriceError):
        Pizza("Test", -10)


def test_pizza_zero_price():
    """Test że zerowa cena rzuca wyjątek."""
    with pytest.raises(InvalidPriceError):
        Pizza("Test", 0)
```

### Sprawdzanie komunikatu wyjątku

```python
def test_pizza_negative_price_message():
    """Test komunikatu wyjątku."""
    with pytest.raises(InvalidPriceError) as exc_info:
        Pizza("Test", -10)

    # Sprawdź komunikat
    assert "-10" in str(exc_info.value)
    assert "cena" in str(exc_info.value).lower()


def test_pizza_invalid_price_attributes():
    """Test atrybutów wyjątku."""
    with pytest.raises(InvalidPriceError) as exc_info:
        Pizza("Test", -10)

    # Sprawdź atrybuty wyjątku
    assert exc_info.value.price == -10
```

### Przykład: Testy wyjątków w Menu

```python
import pytest
from pizza import Pizza, Menu
from exceptions import PizzaNotFoundError


def test_menu_find_not_found_raises():
    """Test że szukanie nieistniejącej pizzy rzuca wyjątek."""
    menu = Menu()

    with pytest.raises(PizzaNotFoundError):
        menu.find_pizza("Nieistniejąca")


def test_menu_find_not_found_message():
    """Test komunikatu wyjątku PizzaNotFoundError."""
    menu = Menu()

    with pytest.raises(PizzaNotFoundError) as exc_info:
        menu.find_pizza("Hawajska")

    assert exc_info.value.pizza_name == "Hawajska"
    assert "Hawajska" in str(exc_info.value)
```

### Ćwiczenie praktyczne (10 min)

**Zadanie:**

1. Napisz testy wyjątków dla Pizza:
   - `test_pizza_negative_price_raises` - ujemna cena rzuca `InvalidPriceError`
   - `test_pizza_zero_price_raises` - zerowa cena rzuca `InvalidPriceError`
   - `test_pizza_empty_name_raises` - pusta nazwa rzuca `ValueError`

2. Napisz testy wyjątków dla Menu:
   - `test_menu_find_not_found` - nieistniejąca pizza rzuca `PizzaNotFoundError`
   - `test_menu_add_duplicate` - duplikat rzuca `ValueError`

3. Uruchom testy:
   ```bash
   pytest tests/test_pizza.py -v
   ```

---

## Część 5: Fixtures - przygotowanie danych

### Teoria: Co to fixture?

**Fixture** to funkcja przygotowująca dane testowe. Pozwala uniknąć powtarzania kodu.

```python
import pytest
from pizza import Pizza, Menu


@pytest.fixture
def sample_pizza():
    """Fixture zwracający przykładową pizzę."""
    return Pizza("Margherita", 25.0)


@pytest.fixture
def sample_menu():
    """Fixture zwracający menu z pizzami."""
    menu = Menu()
    menu.add_pizza(Pizza("Margherita", 25.0))
    menu.add_pizza(Pizza("Pepperoni", 30.0))
    menu.add_pizza(Pizza("Hawajska", 32.0))
    return menu


# Użycie fixture jako parametr funkcji testowej
def test_pizza_name(sample_pizza):
    """Używa fixture sample_pizza."""
    assert sample_pizza.name == "Margherita"


def test_menu_has_pizzas(sample_menu):
    """Używa fixture sample_menu."""
    assert len(sample_menu) == 3
```

### Fixture z cleanup (yield)

```python
import pytest
from customer import Customer


@pytest.fixture
def customer():
    """Fixture z cleanup - resetuje licznik ID."""
    # Setup
    Customer.reset_id_counter()
    customer = Customer("Jan Kowalski", "123-456-789")

    yield customer  # Zwraca fixture

    # Cleanup (wykonane po teście)
    Customer.reset_id_counter()


def test_customer_id(customer):
    """Dzięki fixture każdy test zaczyna od ID=1."""
    assert customer.id == 1
```

### Fixture scope

```python
@pytest.fixture(scope="function")  # Domyślnie - nowy dla każdego testu
def fresh_menu():
    return Menu()


@pytest.fixture(scope="module")  # Jeden dla całego pliku testów
def shared_menu():
    menu = Menu()
    menu.add_pizza(Pizza("Shared", 10.0))
    return menu


@pytest.fixture(scope="session")  # Jeden dla całej sesji testów
def database():
    # Kosztowne połączenie z bazą danych
    db = connect_to_database()
    yield db
    db.close()
```

### Fixture w osobnym pliku (conftest.py)

```python
# tests/conftest.py - Współdzielone fixtures
import pytest
from pizza import Pizza


@pytest.fixture
def sample_pizza():
    """Podstawowy fixture - pojedyncza pizza."""
    return Pizza("Margherita", 25.0)


# Przykład fixture który używa innego fixture:
@pytest.fixture
def two_pizzas(sample_pizza):
    """Fixture zależny od innego fixture."""
    second = Pizza("Pepperoni", 30.0)
    return [sample_pizza, second]
```

Fixtures z `conftest.py` są automatycznie dostępne we wszystkich plikach testowych w tym katalogu.

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

Teraz stwórz kompletny zestaw fixtures dla aplikacji pizzerii!

1. Utwórz plik `tests/conftest.py` z fixtures:
   - `sample_pizza` - pojedyncza pizza
   - `sample_menu` - menu z 3 pizzami (Margherita, Pepperoni, Hawajska)
   - `sample_customer` - zwykły klient (z yield i cleanup: reset_id_counter)
   - `sample_vip` - klient VIP z 15% rabatem (z yield i cleanup)
   - `sample_customer_manager` - manager z 2 klientami
   - `sample_order` - zamówienie z 2 pozycjami

2. Przepisz testy żeby używały fixtures:
   ```python
   def test_menu_find(sample_menu):
       found = sample_menu.find_pizza("Margherita")
       assert found is not None
   ```

3. Uruchom testy:
   ```bash
   pytest tests/ -v
   ```

---

## Część 6: Pełny zestaw testów dla pizzerii

### Zadanie zbiorcze (50 min)

Napisz kompletny zestaw testów dla aplikacji pizzerii.

**Struktura:**
```
tests/
├── conftest.py          # Fixtures
├── test_pizza.py        # Testy Pizza i Menu
├── test_customer.py     # Testy Customer i CustomerManager
└── test_order.py        # Testy Order i OrderManager
```

**tests/test_pizza.py:**
```python
import pytest
from pizza import Pizza, Menu
from exceptions import InvalidPriceError, PizzaNotFoundError


class TestPizza:
    """Testy dla klasy Pizza."""

    def test_creation_valid(self):
        pizza = Pizza("Margherita", 25.0)
        assert pizza.name == "Margherita"
        assert pizza.price == 25.0

    def test_creation_invalid_price(self):
        with pytest.raises(InvalidPriceError):
            Pizza("Test", -10)

    def test_str_representation(self):
        pizza = Pizza("Margherita", 25.0)
        assert str(pizza) == "Margherita: 25.0 zł"

    def test_equality(self):
        pizza1 = Pizza("Margherita", 25.0)
        pizza2 = Pizza("Margherita", 25.0)
        assert pizza1 == pizza2

    def test_update_price_valid(self):
        pizza = Pizza("Margherita", 25.0)
        pizza.update_price(30.0)
        assert pizza.price == 30.0

    def test_update_price_invalid(self):
        pizza = Pizza("Margherita", 25.0)
        with pytest.raises(InvalidPriceError):
            pizza.update_price(-5)


class TestMenu:
    """Testy dla klasy Menu."""

    def test_empty_menu(self):
        menu = Menu()
        assert len(menu) == 0

    def test_add_pizza(self):
        menu = Menu()
        pizza = Pizza("Margherita", 25.0)
        menu.add_pizza(pizza)
        assert len(menu) == 1

    def test_find_existing(self, sample_menu):
        found = sample_menu.find_pizza("Margherita")
        assert found is not None
        assert found.name == "Margherita"

    def test_find_not_existing(self, sample_menu):
        with pytest.raises(PizzaNotFoundError):
            sample_menu.find_pizza("Nieistniejąca")

    def test_add_duplicate(self, sample_menu):
        with pytest.raises(ValueError):
            sample_menu.add_pizza(Pizza("Margherita", 30.0))
```

**tests/test_customer.py:**
```python
import pytest
from customer import Customer, VIPCustomer, CustomerManager
from exceptions import CustomerNotFoundError


class TestCustomer:
    """Testy dla klasy Customer."""

    @pytest.fixture(autouse=True)
    def reset_id(self):
        """Resetuje licznik ID przed każdym testem."""
        Customer.reset_id_counter()

    def test_creation(self):
        customer = Customer("Jan Kowalski", "123-456-789")
        assert customer.name == "Jan Kowalski"
        assert customer.phone == "123-456-789"
        assert customer.id == 1

    def test_id_increments(self):
        c1 = Customer("Jan", "111")
        c2 = Customer("Anna", "222")
        assert c1.id == 1
        assert c2.id == 2

    def test_update_phone(self):
        customer = Customer("Jan", "111")
        customer.update_phone("999")
        assert customer.phone == "999"


class TestVIPCustomer:
    """Testy dla klasy VIPCustomer."""

    @pytest.fixture(autouse=True)
    def reset_id(self):
        Customer.reset_id_counter()

    def test_creation(self):
        vip = VIPCustomer("Anna", "123", 15)
        assert vip.discount_percent == 15
        assert vip.loyalty_points == 0

    def test_apply_discount(self):
        vip = VIPCustomer("Anna", "123", 20)
        discounted = vip.apply_discount(100)
        assert discounted == 80.0

    def test_add_loyalty_points(self):
        vip = VIPCustomer("Anna", "123", 10)
        vip.add_loyalty_points(50)
        assert vip.loyalty_points == 50


class TestCustomerManager:
    """Testy dla klasy CustomerManager."""

    def test_empty(self):
        manager = CustomerManager()
        assert len(manager) == 0

    def test_add_customer(self, sample_customer):
        manager = CustomerManager()
        manager.add_customer(sample_customer)
        assert len(manager) == 1

    def test_find_existing(self, sample_customer_manager, sample_customer):
        found = sample_customer_manager.find_customer(sample_customer.id)
        assert found is not None

    def test_find_not_existing(self, sample_customer_manager):
        with pytest.raises(CustomerNotFoundError):
            sample_customer_manager.find_customer(999)
```

### Uruchomienie wszystkich testów

```bash
# Wszystkie testy
pytest tests/ -v

# Z pokryciem kodu (wymaga pytest-cov)
pip install pytest-cov
pytest tests/ --cov=. --cov-report=html

# Tylko szybkie testy (bez E2E)
pytest tests/ -v -m "not slow"
```

---

## Część 7: Debugowanie z pdb

### Teoria: Co to debugger?

**Debugger** pozwala:
- Zatrzymać program w wybranym miejscu (breakpoint)
- Wykonywać kod krok po kroku
- Sprawdzać wartości zmiennych
- Zmieniać wartości w locie

### pdb - wbudowany debugger Pythona

**Sposoby uruchomienia:**

```python
# 1. Wstawienie breakpointa w kodzie
import pdb; pdb.set_trace()  # Python < 3.7

# 2. Nowoczesny sposób (Python 3.7+)
breakpoint()

# 3. Uruchomienie z linii poleceń
python -m pdb script.py
```

### Komendy pdb

| Komenda | Opis |
|---------|------|
| `n` (next) | Wykonaj następną linię |
| `s` (step) | Wejdź do funkcji |
| `c` (continue) | Kontynuuj do następnego breakpointa |
| `l` (list) | Pokaż kod wokół aktualnej linii |
| `p <expr>` | Wyświetl wartość wyrażenia |
| `pp <expr>` | Pretty-print wyrażenia |
| `w` (where) | Pokaż stos wywołań |
| `q` (quit) | Zakończ debugger |
| `h` (help) | Pomoc |

### Przykład: Debugowanie pizzerii

```python
# pizza.py
class Pizza:
    def __init__(self, name, price):
        breakpoint()  # Tu się zatrzymamy!

        if price <= 0:
            raise InvalidPriceError(price)
        self.name = name
        self.price = price
```

**Sesja debugowania:**

```
> pizza.py(5)__init__()
-> if price <= 0:
(Pdb) p name
'Margherita'
(Pdb) p price
25.0
(Pdb) n
> pizza.py(7)__init__()
-> self.name = name
(Pdb) l
  4         breakpoint()
  5         if price <= 0:
  6             raise InvalidPriceError(price)
  7  ->      self.name = name
  8         self.price = price
(Pdb) c
```

### Ćwiczenie praktyczne (10 min)

**Zadanie:**

1. Dodaj `breakpoint()` w metodzie `Order.add_item()`

2. Uruchom program i przejdź przez wykonanie krok po kroku:
   ```bash
   python main.py
   ```

3. Użyj komend:
   - `p pizza` - sprawdź obiekt pizza
   - `p quantity` - sprawdź ilość
   - `p self.items` - sprawdź listę pozycji przed i po
   - `n` - przejdź do następnej linii
   - `l` - pokaż kod wokół
   - `c` - kontynuuj wykonanie

4. Usuń breakpoint po ćwiczeniu!

---

## Część 8: Debugowanie w PyCharm/VS Code

### PyCharm

**Ustawienie breakpointa:**
- Kliknij na marginesie obok numeru linii (pojawi się czerwona kropka)

**Uruchomienie debuggera:**
- Prawy klik na pliku → "Debug 'nazwa'"
- Lub Shift+F9

**Panel debuggera:**
- **Variables** - wartości wszystkich zmiennych
- **Watches** - śledzenie wybranych wyrażeń
- **Console** - interaktywna konsola Python
- **Frames** - stos wywołań

**Przyciski sterowania:**
| Przycisk | Skrót | Opis |
|----------|-------|------|
| Step Over | F8 | Wykonaj linię (nie wchodź do funkcji) |
| Step Into | F7 | Wejdź do funkcji |
| Step Out | Shift+F8 | Wyjdź z funkcji |
| Resume | F9 | Kontynuuj do następnego breakpointa |
| Stop | Ctrl+F2 | Zatrzymaj debugowanie |

**Warunkowe breakpointy:**
- Prawy klik na breakpoincie → "Edit Breakpoint"
- Wpisz warunek, np. `price < 0`

### VS Code

**Konfiguracja:**
1. Utwórz plik `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

**Breakpointy:**
- Kliknij na marginesie lub F9

**Uruchomienie:**
- F5 lub "Run → Start Debugging"

### Ćwiczenie praktyczne (10 min)

**Zadanie:**

1. Otwórz projekt w PyCharm lub VS Code

2. Ustaw breakpoint w `VIPCustomer.apply_discount()`

3. Uruchom debugger i:
   - Sprawdź wartość `self.discount_percent`
   - Sprawdź wartość parametru `amount`
   - Dodaj watch na wyrażenie: `amount * (1 - self.discount_percent / 100)`

4. Przejdź przez obliczenie rabatu i obserwuj wynik

---

## Część 9: Testy integracyjne i E2E

### Teoria: Rodzaje testów

**Testy jednostkowe (Unit):**
```python
def test_pizza_price():
    """Testuje tylko klasę Pizza w izolacji."""
    pizza = Pizza("Margherita", 25.0)
    assert pizza.price == 25.0
```

**Testy integracyjne (Integration):**
```python
def test_menu_with_pizza():
    """Testuje współpracę Menu i Pizza."""
    menu = Menu()
    pizza = Pizza("Margherita", 25.0)

    menu.add_pizza(pizza)
    found = menu.find_pizza("Margherita")

    assert found == pizza
```

**Testy E2E (End-to-End):**
```python
def test_full_order_flow():
    """Testuje pełny przepływ zamówienia."""
    # Przygotowanie
    menu = Menu()
    menu.add_pizza(Pizza("Margherita", 25.0))
    menu.add_pizza(Pizza("Pepperoni", 30.0))

    customer_manager = CustomerManager()
    vip = VIPCustomer("Anna", "123", 15)
    customer_manager.add_customer(vip)

    order_manager = OrderManager()

    # Akcja - pełny flow użytkownika
    order = order_manager.create_order(vip)
    order.add_item(menu.find_pizza("Margherita"), 2)
    order.add_item(menu.find_pizza("Pepperoni"), 1)

    # Sprawdzenie
    expected_total = (25.0 * 2 + 30.0) * 0.85  # 15% zniżki VIP
    assert order.total_price == expected_total
    assert len(order) == 2
```

### Przykład: Test integracyjny z persystencją

```python
import os
import pytest


@pytest.fixture
def temp_menu_file(tmp_path):
    """Fixture tworzący tymczasowy plik menu."""
    return tmp_path / "menu.json"


def test_menu_save_and_load(temp_menu_file):
    """Test zapisu i odczytu menu do pliku."""
    # Przygotowanie
    menu = Menu()
    menu.add_pizza(Pizza("Margherita", 25.0))
    menu.add_pizza(Pizza("Pepperoni", 30.0))

    # Akcja - zapis
    menu.save_to_file(str(temp_menu_file))

    # Akcja - odczyt do nowego menu
    menu2 = Menu()
    menu2.load_from_file(str(temp_menu_file))

    # Sprawdzenie
    assert len(menu2) == 2
    assert menu2.find_pizza("Margherita").price == 25.0
```

### Test E2E z persystencją

```python
def test_full_application_flow(tmp_path):
    """Test E2E - pełny cykl życia aplikacji."""
    menu_file = tmp_path / "menu.json"
    customers_file = tmp_path / "customers.json"

    # === Sesja 1: Tworzenie danych ===
    menu = Menu()
    menu.add_pizza(Pizza("Margherita", 25.0))
    menu.save_to_file(str(menu_file))

    customer_manager = CustomerManager()
    customer_manager.add_customer(Customer("Jan", "123"))
    customer_manager.save_to_file(str(customers_file))

    # === Sesja 2: Odczyt i użycie ===
    menu2 = Menu()
    menu2.load_from_file(str(menu_file))

    cm2 = CustomerManager()
    cm2.load_from_file(str(customers_file))

    order_manager = OrderManager()
    customer = cm2.customers[0]
    order = order_manager.create_order(customer)
    order.add_item(menu2.find_pizza("Margherita"), 1)

    # Sprawdzenie
    assert order.total_price == 25.0
    assert order.customer.name == "Jan"
```

### Oznaczanie testów

```python
import pytest


@pytest.mark.unit
def test_pizza_creation():
    """Test jednostkowy."""
    pass


@pytest.mark.integration
def test_menu_with_pizza():
    """Test integracyjny."""
    pass


@pytest.mark.e2e
@pytest.mark.slow
def test_full_flow():
    """Test E2E - może być wolny."""
    pass
```

**Uruchamianie wybranych testów:**
```bash
# Tylko testy jednostkowe
pytest -m unit

# Tylko szybkie testy (bez slow)
pytest -m "not slow"

# Testy integracyjne i E2E
pytest -m "integration or e2e"
```

### Ćwiczenie praktyczne (15 min)

**Zadanie:**

1. Napisz test integracyjny `test_order_with_vip_discount`:
   - Utwórz menu z pizzami
   - Utwórz klienta VIP
   - Utwórz zamówienie
   - Sprawdź że rabat jest prawidłowo naliczany

2. Napisz test E2E `test_complete_order_flow`:
   - Pełny flow od dodania pizz do menu po złożenie zamówienia
   - Użyj fixtures z conftest.py

3. Uruchom testy:
   ```bash
   pytest tests/ -v -m "integration or e2e"
   ```

---

## Część 10: Podsumowanie kursu

### Co osiągnęliśmy w Weekend 2?

**Dzień 1 - Wyjątki i I/O:**
- Przechwytywanie wyjątków (try/except)
- Rzucanie wyjątków (raise)
- Własne klasy wyjątków
- Praca z plikami
- Serializacja JSON

**Dzień 2 - Testowanie i debugowanie:**
- Testy jednostkowe z pytest
- Fixtures i organizacja testów
- Testowanie wyjątków
- Debugowanie z pdb
- Debugowanie w IDE
- Testy integracyjne i E2E

### Podsumowanie weekendu 1+2

| Weekend | Tematy |
|---------|--------|
| **Weekend 1** | Proceduralne, OOP, klasy, dziedziczenie |
| **Weekend 2** | Wyjątki, I/O, testy, debugowanie |

### Nasza aplikacja teraz:

```
pizzeria/
├── __init__.py
├── pizza.py           # Klasy Pizza, Menu z walidacją
├── customer.py        # Klasy Customer, VIPCustomer z walidacją
├── order.py           # Klasy Order, OrderManager
├── exceptions.py      # Hierarchia wyjątków
├── main.py            # Punkt wejścia
└── tests/
    ├── conftest.py    # Fixtures
    ├── test_pizza.py
    ├── test_customer.py
    └── test_order.py
```

**Funkcjonalności:**
- Walidacja danych z własnymi wyjątkami
- Persystencja (zapis/odczyt JSON)
- Pełny zestaw testów
- Możliwość debugowania

### Co dalej?

**Tematy do zgłębienia:**
1. **Type hints** - statyczne typowanie w Pythonie
2. **Dataclasses** - prostsze definiowanie klas
3. **Pytest-mock** - mockowanie w testach
4. **Coverage** - analiza pokrycia kodu testami
5. **CI/CD** - automatyczne uruchamianie testów

### Zasoby

- https://docs.pytest.org/
- https://docs.python.org/3/library/pdb.html
- https://realpython.com/python-testing/
- "Test-Driven Development with Python" - Harry Percival

---

## Gratulacje!

Ukończyłeś Weekend 2 kursu Python!

Teraz potrafisz:
- Obsługiwać błędy z własnymi wyjątkami
- Zapisywać i wczytywać dane z plików
- Pisać testy jednostkowe, integracyjne i E2E
- Debugować kod krok po kroku

**Powodzenia w dalszej przygodzie z Pythonem!**
