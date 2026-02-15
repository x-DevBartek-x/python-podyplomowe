import os
import json
from django.shortcuts import render, redirect
from django.http import Http404
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.pizza import Menu
from rozwiazanie_weekend2.customer import CustomerManager
from rozwiazanie_weekend2.exceptions import CustomerNotFoundError, PizzaNotFoundError
from django.contrib import messages

MENU_FILE = os.path.join(DATA_DIR, 'menu.json')
CUSTOMERS_FILE = os.path.join(DATA_DIR, 'customers.json')
ORDERS_FILE = os.path.join(DATA_DIR, 'orders.json')

def _load_orders():
    """Wczytuje zamowienia z pliku JSON."""
    try:
        with open(ORDERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _save_orders(orders_data):
    """Zapisuje zamowienia do pliku JSON."""
    with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(orders_data, f, indent=2, ensure_ascii=False)
        
def order_list(request):
    orders_data = _load_orders()
    customer_mgr = CustomerManager()
    customer_mgr.load_from_file(CUSTOMERS_FILE)

    orders_display = []
    for order_data in orders_data:
        # Znajdz nazwe klienta
        customer_name = f"Klient #{order_data['customer_id']}"
        try:
            customer = customer_mgr.find_customer(order_data['customer_id'])
            customer_name = customer.name
        except CustomerNotFoundError:
            pass

        # Oblicz sume
        total = sum(item['pizza_price'] * item['quantity'] for item in order_data['items'])
        if order_data.get('discount_percent'):
            total = total * (1 - order_data['discount_percent'] / 100)

        orders_display.append({
            'id': order_data['id'],
            'customer_name': customer_name,
            'items_count': len(order_data['items']),
            'total': round(total, 2),
            'is_vip': order_data.get('discount_percent') is not None,
        })

    return render(request, 'orders_app/order_list.html', {'orders': orders_display})

def order_detail(request, order_id):
    orders_data = _load_orders()
    customer_mgr = CustomerManager()
    customer_mgr.load_from_file(CUSTOMERS_FILE)

    # Znajdz zamowienie
    order_data = None
    for o in orders_data:
        if o['id'] == order_id:
            order_data = o
            break

    if order_data is None:
        raise Http404(f"Zamowienie #{order_id} nie znalezione")

    # Nazwa klienta
    customer_name = f"Klient #{order_data['customer_id']}"
    try:
        customer = customer_mgr.find_customer(order_data['customer_id'])
        customer_name = customer.name
    except CustomerNotFoundError:
        pass

    # Pozycje i sumy
    items = []
    subtotal = 0
    for item in order_data['items']:
        item_total = item['pizza_price'] * item['quantity']
        subtotal += item_total
        items.append({
            'pizza_name': item['pizza_name'],
            'pizza_price': item['pizza_price'],
            'quantity': item['quantity'],
            'total': item_total,
        })

    discount_percent = order_data.get('discount_percent')
    discount_amount = 0
    total = subtotal
    if discount_percent:
        discount_amount = round(subtotal * discount_percent / 100, 2)
        total = round(subtotal - discount_amount, 2)

    return render(request, 'orders_app/order_detail.html', {
        'order_id': order_data['id'],
        'customer_name': customer_name,
        'items': items,
        'subtotal': subtotal,
        'discount_percent': discount_percent,
        'discount_amount': discount_amount,
        'total': total,
    })

def order_create(request):
    menu = Menu()
    menu.load_from_file(MENU_FILE)
    customer_mgr = CustomerManager()
    customer_mgr.load_from_file(CUSTOMERS_FILE)

    if request.method == 'POST':
        customer_id_str = request.POST.get('customer_id', '')
        pizza_name = request.POST.get('pizza_name', '')
        quantity_str = request.POST.get('quantity', '1')

        errors = []
        if not customer_id_str:
            errors.append("Wybierz klienta.")
        if not pizza_name:
            errors.append("Wybierz pizze.")

        if not errors:
            try:
                customer_id = int(customer_id_str)
                customer = customer_mgr.find_customer(customer_id)
                pizza = menu.find_pizza(pizza_name)
                quantity = int(quantity_str)

                # Oblicz rabat VIP
                discount_percent = None
                if hasattr(customer, 'discount_percent'):
                    discount_percent = customer.discount_percent

                # Zapisz zamowienie
                orders_data = _load_orders()
                next_id = max((o['id'] for o in orders_data), default=0) + 1
                new_order = {
                    'id': next_id,
                    'customer_id': customer.id,
                    'items': [{
                        'pizza_name': pizza.name,
                        'pizza_price': pizza.price,
                        'quantity': quantity,
                    }],
                    'discount_percent': discount_percent,
                }
                orders_data.append(new_order)
                _save_orders(orders_data)
                messages.success(request, f"Dodano nowe zamówienie: {next_id}")
                return redirect('order_detail', order_id=next_id)
            except CustomerNotFoundError:
                errors.append("Wybrany klient nie istnieje.")
            except PizzaNotFoundError:
                errors.append("Wybrana pizza nie istnieje.")
            except ValueError:
                errors.append("Nieprawidlowe dane.")

        return render(request, 'orders_app/order_form.html', {
            'errors': errors,
            'pizzas': list(menu),
            'customers': list(customer_mgr),
        })

    return render(request, 'orders_app/order_form.html', {
        'pizzas': list(menu),
        'customers': list(customer_mgr),
    })