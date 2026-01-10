# Testy dla klas Order i OrderManager
# Przykład kompletnego zestawu testów

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'dzien1', 'przyklad_wyjatki'))

from pizza import Pizza
from customer import Customer, VIPCustomer
from order import Order, OrderItem, OrderManager
from exceptions import (
    InvalidQuantityError,
    OrderNotFoundError,
    EmptyOrderError
)


class TestOrderItem:
    """Testy dla klasy OrderItem."""

    def test_creation(self, sample_pizza):
        """Test tworzenia pozycji zamówienia."""
        item = OrderItem(sample_pizza, 2)

        assert item.pizza == sample_pizza
        assert item.quantity == 2

    def test_total_price(self, sample_pizza):
        """Test obliczania ceny pozycji."""
        item = OrderItem(sample_pizza, 2)  # 2 x 25 = 50

        assert item.total_price == 50.0

    def test_invalid_quantity_zero_raises(self, sample_pizza):
        """Test że ilość 0 rzuca wyjątek."""
        with pytest.raises(InvalidQuantityError):
            OrderItem(sample_pizza, 0)

    def test_invalid_quantity_negative_raises(self, sample_pizza):
        """Test że ujemna ilość rzuca wyjątek."""
        with pytest.raises(InvalidQuantityError) as exc_info:
            OrderItem(sample_pizza, -2)

        assert exc_info.value.quantity == -2

    def test_non_pizza_raises(self):
        """Test że nie-pizza rzuca TypeError."""
        with pytest.raises(TypeError):
            OrderItem("nie pizza", 1)

    def test_str_representation(self, sample_pizza):
        """Test reprezentacji tekstowej."""
        item = OrderItem(sample_pizza, 2)

        result = str(item)

        assert "2x" in result
        assert "Margherita" in result
        assert "50" in result


class TestOrder:
    """Testy dla klasy Order."""

    def test_creation(self, sample_customer, reset_order_id):
        """Test tworzenia zamówienia."""
        order = Order(sample_customer)

        assert order.customer == sample_customer
        assert len(order) == 0
        assert order.id == 1

    def test_id_increments(self, sample_customer, reset_order_id):
        """Test że ID są sekwencyjne."""
        o1 = Order(sample_customer)
        o2 = Order(sample_customer)

        assert o1.id == 1
        assert o2.id == 2

    def test_non_customer_raises(self, reset_order_id):
        """Test że nie-klient rzuca TypeError."""
        with pytest.raises(TypeError):
            Order("nie klient")

    def test_add_item(self, sample_customer, sample_pizza, reset_order_id):
        """Test dodawania pozycji."""
        order = Order(sample_customer)

        order.add_item(sample_pizza, 2)

        assert len(order) == 1

    def test_add_multiple_items(self, sample_customer, sample_menu, reset_order_id):
        """Test dodawania wielu pozycji."""
        order = Order(sample_customer)

        order.add_item(sample_menu.find_pizza("Margherita"), 1)
        order.add_item(sample_menu.find_pizza("Pepperoni"), 2)

        assert len(order) == 2

    def test_total_price(self, sample_customer, sample_menu, reset_order_id):
        """Test obliczania łącznej ceny."""
        order = Order(sample_customer)
        order.add_item(sample_menu.find_pizza("Margherita"), 2)  # 2 x 25 = 50
        order.add_item(sample_menu.find_pizza("Pepperoni"), 1)   # 1 x 30 = 30

        assert order.total_price == 80.0

    def test_total_price_with_vip_discount(self, sample_vip, sample_menu, reset_order_id):
        """Test ceny z rabatem VIP."""
        order = Order(sample_vip)  # 15% rabatu
        order.add_item(sample_menu.find_pizza("Margherita"), 2)  # 2 x 25 = 50

        expected = 50 * 0.85  # 42.5
        assert order.total_price == expected

    def test_remove_item(self, sample_customer, sample_menu, reset_order_id):
        """Test usuwania pozycji."""
        order = Order(sample_customer)
        order.add_item(sample_menu.find_pizza("Margherita"), 1)
        order.add_item(sample_menu.find_pizza("Pepperoni"), 1)

        result = order.remove_item("Margherita")

        assert result is True
        assert len(order) == 1

    def test_remove_nonexistent_item(self, sample_customer, reset_order_id):
        """Test usuwania nieistniejącej pozycji."""
        order = Order(sample_customer)

        result = order.remove_item("Nieistniejąca")

        assert result is False

    def test_process_with_items(self, sample_order):
        """Test przetwarzania zamówienia z pozycjami."""
        # Nie powinno rzucić wyjątku
        sample_order.process()

    def test_process_empty_raises(self, sample_customer, reset_order_id):
        """Test że przetwarzanie pustego zamówienia rzuca wyjątek."""
        order = Order(sample_customer)

        with pytest.raises(EmptyOrderError) as exc_info:
            order.process()

        assert exc_info.value.order_id == order.id


class TestOrderManager:
    """Testy dla klasy OrderManager."""

    def test_empty(self):
        """Test pustego managera."""
        manager = OrderManager()

        assert len(manager) == 0

    def test_create_order(self, empty_order_manager, sample_customer):
        """Test tworzenia zamówienia."""
        order = empty_order_manager.create_order(sample_customer)

        assert order is not None
        assert len(empty_order_manager) == 1

    def test_find_existing(self, sample_order_manager):
        """Test znajdowania istniejącego zamówienia."""
        # sample_order_manager ma 2 zamówienia z ID 1 i 2
        found = sample_order_manager.find_order(1)

        assert found is not None

    def test_find_not_existing_raises(self, sample_order_manager):
        """Test że szukanie nieistniejącego zamówienia rzuca wyjątek."""
        with pytest.raises(OrderNotFoundError) as exc_info:
            sample_order_manager.find_order(999)

        assert exc_info.value.order_id == 999

    def test_cancel_order(self, sample_order_manager):
        """Test anulowania zamówienia."""
        initial_count = len(sample_order_manager)

        sample_order_manager.cancel_order(1)

        assert len(sample_order_manager) == initial_count - 1

    def test_cancel_nonexistent_raises(self, sample_order_manager):
        """Test że anulowanie nieistniejącego zamówienia rzuca wyjątek."""
        with pytest.raises(OrderNotFoundError):
            sample_order_manager.cancel_order(999)

    def test_get_total_revenue(self, sample_order_manager):
        """Test obliczania łącznego przychodu."""
        revenue = sample_order_manager.get_total_revenue()

        # Zamówienie 1: 2 x 25 = 50
        # Zamówienie 2 (VIP 15%): 1 x 30 * 0.85 = 25.5
        expected = 50 + 25.5
        assert revenue == pytest.approx(expected)

    def test_iter(self, sample_order_manager):
        """Test iteracji po zamówieniach."""
        orders = list(sample_order_manager)

        assert len(orders) == 2


class TestIntegration:
    """Testy integracyjne."""

    def test_full_order_flow(self, sample_menu, reset_customer_id, reset_order_id):
        """Test pełnego flow zamówienia."""
        # Tworzenie klienta VIP
        vip = VIPCustomer("Test VIP", "123", 20)

        # Tworzenie zamówienia
        order_manager = OrderManager()
        order = order_manager.create_order(vip)

        # Dodawanie pozycji
        order.add_item(sample_menu.find_pizza("Margherita"), 2)
        order.add_item(sample_menu.find_pizza("Pepperoni"), 1)

        # Sprawdzenie ceny (z 20% rabatem)
        subtotal = 2 * 25 + 1 * 30  # 80
        expected = subtotal * 0.80  # 64
        assert order.total_price == expected

        # Przetworzenie zamówienia
        order.process()  # Nie powinno rzucić wyjątku

        # Sprawdzenie przychodu
        assert order_manager.get_total_revenue() == expected
