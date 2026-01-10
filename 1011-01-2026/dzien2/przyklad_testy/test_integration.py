# Testy integracyjne i E2E
# Przykłady testów wyższego poziomu

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'dzien1', 'przyklad_wyjatki'))

from pizza import Pizza, Menu
from customer import Customer, VIPCustomer, CustomerManager
from order import Order, OrderManager


class TestMenuCustomerIntegration:
    """Testy integracji Menu z Customer."""

    def test_vip_gets_discount_on_pizza(self, sample_menu, sample_vip):
        """Test że VIP dostaje rabat na pizzę."""
        pizza = sample_menu.find_pizza("Margherita")
        original_price = pizza.price

        discounted = sample_vip.apply_discount(original_price)

        assert discounted < original_price
        assert discounted == original_price * 0.85  # 15% rabatu


class TestOrderIntegration:
    """Testy integracji Order z innymi komponentami."""

    def test_order_with_menu_and_customer(
        self, sample_menu, sample_customer, reset_order_id
    ):
        """Test zamówienia używającego menu i klienta."""
        order = Order(sample_customer)

        # Dodaj pizze z menu
        pizza1 = sample_menu.find_pizza("Margherita")
        pizza2 = sample_menu.find_pizza("Pepperoni")

        order.add_item(pizza1, 1)
        order.add_item(pizza2, 2)

        assert len(order) == 2
        assert order.total_price == 25 + 60  # 1x25 + 2x30

    def test_vip_order_discount_calculation(
        self, sample_menu, sample_vip, reset_order_id
    ):
        """Test że zamówienie VIP poprawnie nalicza rabat."""
        order = Order(sample_vip)  # 15% rabatu

        order.add_item(sample_menu.find_pizza("Margherita"), 4)  # 4 x 25 = 100

        expected = 100 * 0.85  # 85
        assert order.total_price == expected


class TestPersistenceIntegration:
    """Testy integracji z persystencją."""

    def test_menu_roundtrip(self, sample_menu, temp_menu_file):
        """Test że menu zachowuje dane po zapisie i odczycie."""
        # Zapis
        sample_menu.save_to_file(str(temp_menu_file))

        # Odczyt
        loaded = Menu()
        loaded.load_from_file(str(temp_menu_file))

        # Porównanie
        assert len(loaded) == len(sample_menu)

        for pizza in sample_menu:
            found = loaded.find_pizza(pizza.name)
            assert found.price == pizza.price

    def test_customers_roundtrip(
        self, sample_customer_manager, temp_customers_file, reset_customer_id
    ):
        """Test że klienci zachowują dane po zapisie i odczycie."""
        # Zapis
        sample_customer_manager.save_to_file(str(temp_customers_file))

        # Reset licznika i odczyt
        Customer.reset_id_counter()
        loaded = CustomerManager()
        loaded.load_from_file(str(temp_customers_file))

        # Porównanie
        assert len(loaded) == len(sample_customer_manager)

        # Sprawdź typy
        has_vip = any(isinstance(c, VIPCustomer) for c in loaded)
        assert has_vip


class TestE2E:
    """Testy End-to-End - pełny flow aplikacji."""

    def test_complete_application_flow(self, tmp_path):
        """Test pełnego cyklu życia aplikacji."""
        menu_file = tmp_path / "menu.json"
        customers_file = tmp_path / "customers.json"

        # === SESJA 1: Tworzenie danych ===
        Customer.reset_id_counter()
        Order.reset_id_counter()

        # Tworzenie menu
        menu = Menu()
        menu.add_pizza(Pizza("Margherita", 25.0))
        menu.add_pizza(Pizza("Pepperoni", 30.0))
        menu.add_pizza(Pizza("Hawajska", 32.0))
        menu.save_to_file(str(menu_file))

        # Tworzenie klientów
        customer_manager = CustomerManager()
        customer_manager.add_customer(Customer("Jan Kowalski", "123"))
        customer_manager.add_customer(VIPCustomer("Anna Nowak", "456", 15))
        customer_manager.save_to_file(str(customers_file))

        # Tworzenie zamówień
        order_manager = OrderManager()

        customer = customer_manager.find_customer(1)
        order1 = order_manager.create_order(customer)
        order1.add_item(menu.find_pizza("Margherita"), 2)

        vip = customer_manager.find_customer(2)
        order2 = order_manager.create_order(vip)
        order2.add_item(menu.find_pizza("Pepperoni"), 1)

        revenue_session1 = order_manager.get_total_revenue()

        # === SESJA 2: Wczytywanie i kontynuacja ===
        Customer.reset_id_counter()
        Order.reset_id_counter()

        # Wczytanie danych
        menu2 = Menu()
        menu2.load_from_file(str(menu_file))

        cm2 = CustomerManager()
        cm2.load_from_file(str(customers_file))

        # Sprawdzenie że dane są kompletne
        assert len(menu2) == 3
        assert len(cm2) == 2

        # Nowe zamówienie
        om2 = OrderManager()
        new_customer = cm2.find_customer(1)
        new_order = om2.create_order(new_customer)
        new_order.add_item(menu2.find_pizza("Hawajska"), 1)

        # Sprawdzenie
        assert new_order.total_price == 32.0
        assert new_order.customer.name == "Jan Kowalski"

    def test_error_handling_in_flow(self, sample_menu, sample_customer, reset_order_id):
        """Test obsługi błędów w pełnym flow."""
        from exceptions import PizzaNotFoundError, EmptyOrderError

        order_manager = OrderManager()
        order = order_manager.create_order(sample_customer)

        # Próba dodania nieistniejącej pizzy
        with pytest.raises(PizzaNotFoundError):
            pizza = sample_menu.find_pizza("Nieistniejąca")
            order.add_item(pizza, 1)

        # Próba przetworzenia pustego zamówienia
        with pytest.raises(EmptyOrderError):
            order.process()

        # Po dodaniu pozycji powinno działać
        pizza = sample_menu.find_pizza("Margherita")
        order.add_item(pizza, 1)
        order.process()  # Nie rzuca wyjątku

    def test_statistics_calculation(self, sample_menu, reset_customer_id, reset_order_id):
        """Test obliczania statystyk."""
        # Klienci
        customer1 = Customer("Jan", "111")
        vip = VIPCustomer("Anna", "222", 20)

        # Zamówienia
        order_manager = OrderManager()

        # Zamówienie 1: 2 x Margherita (2 x 25 = 50)
        o1 = order_manager.create_order(customer1)
        o1.add_item(sample_menu.find_pizza("Margherita"), 2)

        # Zamówienie 2 (VIP 20%): 1 x Pepperoni (30 * 0.8 = 24)
        o2 = order_manager.create_order(vip)
        o2.add_item(sample_menu.find_pizza("Pepperoni"), 1)

        # Zamówienie 3: 1 x Hawajska (32)
        o3 = order_manager.create_order(customer1)
        o3.add_item(sample_menu.find_pizza("Hawajska"), 1)

        # Sprawdzenie statystyk
        total_revenue = order_manager.get_total_revenue()
        expected = 50 + 24 + 32  # 106

        assert total_revenue == expected
        assert len(order_manager) == 3

        # Statystyki menu
        assert sample_menu.get_cheapest().name == "Margherita"
        assert sample_menu.get_most_expensive().name == "Hawajska"
        assert sample_menu.get_average_price() == pytest.approx(29.0)
