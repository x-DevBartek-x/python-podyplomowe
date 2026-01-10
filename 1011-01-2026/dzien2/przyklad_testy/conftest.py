# conftest.py - Współdzielone fixtures dla testów
# Ten plik jest automatycznie ładowany przez pytest

import pytest
import sys
import os

# Dodaj ścieżkę do modułów z dnia 1
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'dzien1', 'przyklad_wyjatki'))

from pizza import Pizza, Menu
from customer import Customer, VIPCustomer, CustomerManager
from order import Order, OrderManager


# === Fixtures dla Pizza ===

@pytest.fixture
def sample_pizza():
    """Fixture zwracający pojedynczą pizzę."""
    return Pizza("Margherita", 25.0)


@pytest.fixture
def pizza_pepperoni():
    """Fixture dla pizzy Pepperoni."""
    return Pizza("Pepperoni", 30.0)


@pytest.fixture
def pizza_hawajska():
    """Fixture dla pizzy Hawajskiej."""
    return Pizza("Hawajska", 32.0)


# === Fixtures dla Menu ===

@pytest.fixture
def empty_menu():
    """Fixture dla pustego menu."""
    return Menu()


@pytest.fixture
def sample_menu():
    """Fixture dla menu z 3 pizzami."""
    menu = Menu()
    menu.add_pizza(Pizza("Margherita", 25.0))
    menu.add_pizza(Pizza("Pepperoni", 30.0))
    menu.add_pizza(Pizza("Hawajska", 32.0))
    return menu


# === Fixtures dla Customer ===

@pytest.fixture(autouse=False)
def reset_customer_id():
    """Fixture resetujący licznik ID klientów."""
    Customer.reset_id_counter()
    yield
    Customer.reset_id_counter()


@pytest.fixture
def sample_customer(reset_customer_id):
    """Fixture dla zwykłego klienta."""
    return Customer("Jan Kowalski", "123-456-789")


@pytest.fixture
def sample_vip(reset_customer_id):
    """Fixture dla klienta VIP."""
    return VIPCustomer("Anna Nowak", "987-654-321", 15)


@pytest.fixture
def vip_20_percent(reset_customer_id):
    """Fixture dla VIP z 20% rabatem."""
    return VIPCustomer("Piotr Wiśniewski", "555-123-456", 20)


# === Fixtures dla CustomerManager ===

@pytest.fixture
def empty_customer_manager():
    """Fixture dla pustego managera klientów."""
    return CustomerManager()


@pytest.fixture
def sample_customer_manager(sample_customer, sample_vip):
    """Fixture dla managera z 2 klientami."""
    manager = CustomerManager()
    manager.add_customer(sample_customer)
    manager.add_customer(sample_vip)
    return manager


# === Fixtures dla Order ===

@pytest.fixture(autouse=False)
def reset_order_id():
    """Fixture resetujący licznik ID zamówień."""
    Order.reset_id_counter()
    yield
    Order.reset_id_counter()


@pytest.fixture
def sample_order(sample_customer, sample_pizza, reset_order_id):
    """Fixture dla zamówienia z 1 pozycją."""
    order = Order(sample_customer)
    order.add_item(sample_pizza, 2)
    return order


@pytest.fixture
def vip_order(sample_vip, sample_menu, reset_order_id):
    """Fixture dla zamówienia VIP."""
    order = Order(sample_vip)
    pizza = sample_menu.find_pizza("Margherita")
    order.add_item(pizza, 1)
    return order


# === Fixtures dla OrderManager ===

@pytest.fixture
def empty_order_manager():
    """Fixture dla pustego managera zamówień."""
    return OrderManager()


@pytest.fixture
def sample_order_manager(sample_customer, sample_vip, sample_menu, reset_order_id):
    """Fixture dla managera z 2 zamówieniami."""
    manager = OrderManager()

    # Zamówienie 1
    order1 = manager.create_order(sample_customer)
    order1.add_item(sample_menu.find_pizza("Margherita"), 2)

    # Zamówienie 2 (VIP)
    order2 = manager.create_order(sample_vip)
    order2.add_item(sample_menu.find_pizza("Pepperoni"), 1)

    return manager


# === Fixtures dla plików tymczasowych ===

@pytest.fixture
def temp_menu_file(tmp_path):
    """Fixture zwracający ścieżkę do tymczasowego pliku menu."""
    return tmp_path / "menu.json"


@pytest.fixture
def temp_customers_file(tmp_path):
    """Fixture zwracający ścieżkę do tymczasowego pliku klientów."""
    return tmp_path / "customers.json"
