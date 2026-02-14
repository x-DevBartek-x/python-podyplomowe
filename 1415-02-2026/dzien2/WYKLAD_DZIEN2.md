# Dzien 2: Django - Pelna aplikacja webowa

## Czesc 1: Recap + Detail Views (30 min)

### Recap dnia 1
- Git: init, add, commit, branch, merge, push
- Django: project, views, templates, URL routing
- Otworzylimy gotowy szkielet projektu `pizzeria_django/` (settings, base.html, static)
- Stworzylismy `menu_app` przez `startapp` i zarejestrowalismy go w INSTALLED_APPS + urls.py
- `rozwiazanie_weekend2/` jest skopiowany do srodka `pizzeria_django/` - importy dzialaja bez dodatkowej konfiguracji
- Importy: `from rozwiazanie_weekend2.pizza import Pizza, Menu`, `from rozwiazanie_weekend2 import DATA_DIR`
- pizza_list dziala w przegladarce

### SHOW: Detail view z parametrem URL (GENERIC: ksiazka)

```python
# views.py
def book_detail(request, pk):
    books = {
        1: {'title': 'Python Crash Course', 'author': 'Eric Matthes'},
        2: {'title': 'Fluent Python', 'author': 'Luciano Ramalho'},
    }
    book = books.get(pk)
    if not book:
        raise Http404("Ksiazka nie znaleziona")
    return render(request, 'books/book_detail.html', {'book': book})
```

```python
# urls.py
path('books/<int:pk>/', views.book_detail, name='book_detail'),
```

### DO: pizza_detail view

Cel: po kliknieciu na nazwe pizzy w liscie, zobaczysz strone ze szczegolami tej pizzy.

**Krok 1:** Dodaj nowy view w `menu_app/views.py`:

```python
# menu_app/views.py - dodaj do istniejacego pliku
from django.http import Http404
from rozwiazanie_weekend2.exceptions import PizzaNotFoundError

def pizza_detail(request, name):
    menu = Menu()
    menu.load_from_file(MENU_FILE)
    try:
        pizza = menu.find_pizza(name)
    except PizzaNotFoundError:
        raise Http404(f"Pizza '{name}' nie znaleziona")
    return render(request, 'menu_app/pizza_detail.html', {'pizza': pizza})
```

Zwroc uwage:
- `name` w argumencie funkcji - pochodzi z URL (patrz krok 3)
- `menu.find_pizza(name)` - uzywa metody z naszego engine, ktora rzuca `PizzaNotFoundError`
- `raise Http404(...)` - Django wyswietli strone "404 Not Found"

**Krok 2:** Stworz template `menu_app/templates/menu_app/pizza_detail.html`:

```html
<!DOCTYPE html>
<html>
<head><title>{{ pizza.name }}</title></head>
<body>
    <h1>{{ pizza.name }}</h1>
    <p>Cena: {{ pizza.price }} zl</p>
    <a href="/menu/">Powrot do menu</a>
</body>
</html>
```

Na razie uzywamy prostego HTML (tak jak w pizza_list z dnia 1). W nastepnym cwiczeniu dodamy base.html i przelaczymy na `{% extends %}`.

**Krok 3:** Dodaj URL w `menu_app/urls.py`:

```python
# menu_app/urls.py
path('<str:name>/', views.pizza_detail, name='pizza_detail'),
```

`<str:name>` oznacza: "weź cokolwiek z URL i przekaz jako argument `name` do view".
Np. URL `/menu/Margherita/` -> `pizza_detail(request, name='Margherita')`.

**Krok 4:** Dodaj linki w `pizza_list.html` zeby mozna bylo kliknac na pizze:

```html
{% for pizza in pizzas %}
    <li><a href="/menu/{{ pizza.name }}/">{{ pizza.name }}</a> - {{ pizza.price }} zl</li>
{% endfor %}
```

**Krok 5:** Sprawdz! Wejdz na /menu/, kliknij na nazwe pizzy. Sprobuj tez wejsc na /menu/NieIstniejaca/ - powinienes zobaczyc 404.

---

## Czesc 2: Static Files + Bootstrap (25 min)

### SHOW: base.html z Bootstrap CDN

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Pizzeria{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/menu/">Pizzeria</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/menu/">Menu</a>
                <a class="nav-link" href="/klienci/">Klienci</a>
                <a class="nav-link" href="/zamowienia/">Zamowienia</a>
            </div>
        </div>
    </nav>
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### Settings.py dla static files

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

### DO: Ostyluj pizza pages

Cel: dodaj wspolny wyglad (nawigacja, Bootstrap) do wszystkich stron pizzerii.

**Dobra wiadomosc:** `base.html` i `static/css/style.css` sa juz gotowe w szkielecie projektu! Otworz `templates/base.html` i przejrzyj co jest w srodku - nawigacja, Bootstrap CDN, bloki `{% block title %}` i `{% block content %}`.

Teraz zaktualizuj swoje szablony zeby z niego korzystaly:

**Krok 1:** Zmien `pizza_list.html` zeby uzywal base.html:

```html
{% extends "base.html" %}

{% block title %}Menu{% endblock %}

{% block content %}
<h1>Menu Pizzerii</h1>
<ul>
{% for pizza in pizzas %}
    <li><a href="/menu/{{ pizza.name }}/">{{ pizza.name }}</a> - {{ pizza.price }} zl</li>
{% endfor %}
</ul>
{% endblock %}
```

**Krok 2:** Zmien tez `pizza_detail.html` - zastap caly prosty HTML na:

```html
{% extends "base.html" %}

{% block title %}{{ pizza.name }}{% endblock %}

{% block content %}
<h1>{{ pizza.name }}</h1>
<p>Cena: {{ pizza.price }} zl</p>
<a href="/menu/">Powrot do menu</a>
{% endblock %}
```

Porownaj z wersja z poprzedniego cwiczenia - zamiast calego `<!DOCTYPE html>...` mamy tylko tresc strony. Reszta (head, nav, bootstrap) jest w `base.html`.

**Krok 3:** Sprawdz! Odswierz strone - powinienes zobaczyc ciemna nawigacje na gorze i ostylowana tresc.

Jesli widzisz blad "TemplateDoesNotExist: base.html" - sprawdz czy w `settings.py` masz:
```python
TEMPLATES = [{'DIRS': [BASE_DIR / 'templates'], ...}]
```
(To juz powinno byc skonfigurowane w szkielecie)

---

## Czesc 3: Formularze HTML (30 min)

### SHOW: Formularz kontaktowy (GENERIC)

```python
# views.py
from django.shortcuts import redirect

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Przetwarzanie...
        return redirect('contact_success')
    return render(request, 'contact_form.html')
```

```html
<!-- contact_form.html -->
<form method="post">
    {% csrf_token %}
    <input type="text" name="name" required>
    <input type="email" name="email" required>
    <textarea name="message" required></textarea>
    <button type="submit">Wyslij</button>
</form>
```

### Kluczowe elementy:
1. `method="post"` - wysylanie danych
2. `{% csrf_token %}` - ochrona przed CSRF
3. `request.POST.get('name')` - odczyt danych
4. `redirect()` - przekierowanie po sukcesie

### DO: Formularz dodawania pizzy

Cel: stworz strone /menu/dodaj/ z formularzem do dodawania nowej pizzy do menu.

**Krok 1:** Stworz template `menu_app/templates/menu_app/pizza_form.html`:

```html
{% extends "base.html" %}

{% block title %}Dodaj pizze{% endblock %}

{% block content %}
<h1>Dodaj nowa pizze</h1>

{% if errors %}
<div style="color: red;">
    {% for error in errors %}
    <p>{{ error }}</p>
    {% endfor %}
</div>
{% endif %}

<form method="post">
    {% csrf_token %}
    <div>
        <label>Nazwa:</label>
        <input type="text" name="name" value="{{ name }}" required>
    </div>
    <div>
        <label>Cena (zl):</label>
        <input type="number" name="price" step="0.01" value="{{ price }}" required>
    </div>
    <button type="submit">Dodaj</button>
</form>

<a href="/menu/">Powrot do menu</a>
{% endblock %}
```

Zwroc uwage:
- `{% csrf_token %}` - **WYMAGANE** w kazdym formularzu POST w Django (ochrona przed atakami CSRF)
- `method="post"` - dane ida w body requestu, nie w URL
- `value="{{ name }}"` - zachowuje wpisana wartosc gdy formularz sie nie powiedzie

**Krok 2:** Dodaj view w `menu_app/views.py`:

```python
from django.shortcuts import redirect
from rozwiazanie_weekend2.pizza import Pizza, Menu
from rozwiazanie_weekend2.exceptions import InvalidPriceError, DuplicatePizzaError

def pizza_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        price_str = request.POST.get('price', '').strip()
        try:
            price = float(price_str)
            pizza = Pizza(name, price)
            menu = Menu()
            menu.load_from_file(MENU_FILE)
            menu.add_pizza(pizza)
            menu.save_to_file(MENU_FILE)
            return redirect('pizza_list')
        except (ValueError, InvalidPriceError, DuplicatePizzaError) as e:
            return render(request, 'menu_app/pizza_form.html', {
                'errors': [str(e)],
                'name': name,
                'price': price_str,
            })
    return render(request, 'menu_app/pizza_form.html')
```

Zwroc uwage na wzorzec:
- `if request.method == 'POST'` - formularz zostal wyslany -> przetwarzaj dane
- `else` (GET) - uzytkownik dopiero wchodzi na strone -> pokaz pusty formularz
- `redirect('pizza_list')` - po sukcesie przekieruj na liste (zeby F5 nie wyslal formularza ponownie)
- `except` - przy bledzie pokaz formularz ponownie z komunikatem bledu

**Krok 3:** Dodaj URL w `menu_app/urls.py`:

```python
path('dodaj/', views.pizza_add, name='pizza_add'),
```

**WAZNE:** `dodaj/` musi byc PRZED `<str:name>/` w liscie URL, bo inaczej Django potraktuje "dodaj" jako nazwe pizzy!

```python
# menu_app/urls.py - poprawna kolejnosc
urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('dodaj/', views.pizza_add, name='pizza_add'),        # PRZED <str:name>
    path('<str:name>/', views.pizza_detail, name='pizza_detail'),
]
```

**Krok 4:** Dodaj link w `pizza_list.html`:

```html
<a href="/menu/dodaj/">Dodaj nowa pizze</a>
```

**Krok 5:** Sprawdz! Wejdz na /menu/dodaj/, wypelnij formularz, kliknij "Dodaj". Nowa pizza powinna pojawic sie na liscie.

---

## Czesc 4: Error Handling w Views (20 min)

### SHOW: Obsluga bledow

```python
from django.http import Http404
from rozwiazanie_weekend2.exceptions import PizzaNotFoundError

def pizza_detail(request, name):
    try:
        pizza = menu.find_pizza(name)
    except PizzaNotFoundError:
        raise Http404(f"Pizza '{name}' nie znaleziona")
    return render(request, 'menu_app/pizza_detail.html', {'pizza': pizza})
```

### Wzorzec: try/except w views

```python
def pizza_add(request):
    if request.method == 'POST':
        errors = []
        # ... walidacja ...
        if not errors:
            try:
                # ... operacja ...
                messages.success(request, "Sukces!")
                return redirect('pizza_list')
            except SomeError as e:
                errors.append(str(e))
        return render(request, 'form.html', {'errors': errors})
    return render(request, 'form.html')
```

### DO: Error handling w formularzu

Cel: formularz dodawania pizzy powinien wyswietlac czytelne komunikaty bledow.

**Krok 1:** Zaktualizuj view `pizza_add` - dodaj walidacje PRZED proba utworzenia pizzy:

```python
def pizza_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        price_str = request.POST.get('price', '').strip()

        errors = []
        if not name:
            errors.append("Nazwa pizzy jest wymagana.")
        if not price_str:
            errors.append("Cena jest wymagana.")

        if not errors:
            try:
                price = float(price_str)
                pizza = Pizza(name, price)
                menu = Menu()
                menu.load_from_file(MENU_FILE)
                menu.add_pizza(pizza)
                menu.save_to_file(MENU_FILE)
                return redirect('pizza_list')
            except (ValueError, TypeError) as e:
                errors.append(str(e))
            except InvalidPriceError as e:
                errors.append(str(e))
            except DuplicatePizzaError as e:
                errors.append(str(e))

        return render(request, 'menu_app/pizza_form.html', {
            'errors': errors,
            'name': name,
            'price': price_str,
        })

    return render(request, 'menu_app/pizza_form.html')
```

**Krok 2:** Przetestuj bledy:
- Wyslij pusty formularz -> "Nazwa pizzy jest wymagana."
- Wpisz cene -5 -> blad z `InvalidPriceError`
- Wpisz nazwe pizzy ktora juz istnieje (np. "Margherita") -> blad z `DuplicatePizzaError`
- Wpisz "abc" jako cene -> blad z `ValueError`

---

## Czesc 5: Customer Views (40 min)

### SHOW: Lista klientow + dodawanie

```python
# customers_app/views.py
import os
from django.shortcuts import render, redirect
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.customer import Customer, VIPCustomer, CustomerManager

CUSTOMERS_FILE = os.path.join(DATA_DIR, 'customers.json')

def customer_list(request):
    manager = CustomerManager()
    manager.load_from_file(CUSTOMERS_FILE)
    return render(request, 'customers_app/customer_list.html', {
        'customers': list(manager),
    })

def customer_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        customer_type = request.POST.get('type', 'regular')

        manager = CustomerManager()
        manager.load_from_file(CUSTOMERS_FILE)

        if customer_type == 'vip':
            discount = float(request.POST.get('discount', 10))
            customer = VIPCustomer(name, phone, discount)
        else:
            customer = Customer(name, phone)

        manager.add_customer(customer)
        manager.save_to_file(CUSTOMERS_FILE)
        return redirect('customer_list')

    return render(request, 'customers_app/customer_form.html')
```

### DO: Pelne customers_app

Cel: zbuduj nowy app do zarzadzania klientami - lista klientow + formularz dodawania (z wyborem typu regular/VIP).

**Krok 1:** Stworz nowy app:

```bash
python3 manage.py startapp customers_app
```

**WAZNE - 2 kroki konfiguracji (tak samo jak dla menu_app):**

**A)** Dodaj `'customers_app'` do `INSTALLED_APPS` w `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'menu_app',
    'customers_app',    # <- DODAJ
]
```

**B)** Dodaj routing w glownym `pizzeria_project/urls.py`:

```python
urlpatterns = [
    path('menu/', include('menu_app.urls')),
    path('klienci/', include('customers_app.urls')),    # <- DODAJ
]
```

**Krok 2:** Stworz `customers_app/views.py`:

```python
import os
from django.shortcuts import render, redirect
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.customer import Customer, VIPCustomer, CustomerManager

CUSTOMERS_FILE = os.path.join(DATA_DIR, 'customers.json')

def customer_list(request):
    manager = CustomerManager()
    manager.load_from_file(CUSTOMERS_FILE)
    return render(request, 'customers_app/customer_list.html', {
        'customers': list(manager),
    })

def customer_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        customer_type = request.POST.get('type', 'regular')

        errors = []
        if not name:
            errors.append("Imie klienta jest wymagane.")
        if not phone:
            errors.append("Numer telefonu jest wymagany.")

        if not errors:
            manager = CustomerManager()
            manager.load_from_file(CUSTOMERS_FILE)

            if customer_type == 'vip':
                discount = float(request.POST.get('discount', 10))
                customer = VIPCustomer(name, phone, discount)
            else:
                customer = Customer(name, phone)

            manager.add_customer(customer)
            manager.save_to_file(CUSTOMERS_FILE)
            return redirect('customer_list')

        return render(request, 'customers_app/customer_form.html', {
            'errors': errors,
            'name': name,
            'phone': phone,
        })

    return render(request, 'customers_app/customer_form.html')
```

**Krok 3:** Stworz `customers_app/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('dodaj/', views.customer_add, name='customer_add'),
]
```

Routing glowny (`pizzeria_project/urls.py`) juz podpielismy w Kroku 1B.

**Krok 4:** Stworz template `customers_app/templates/customers_app/customer_list.html`:

```html
{% extends "base.html" %}

{% block title %}Klienci{% endblock %}

{% block content %}
<h1>Lista klientow</h1>
<a href="/klienci/dodaj/">Dodaj klienta</a>

<table>
    <tr><th>ID</th><th>Imie</th><th>Telefon</th><th>Typ</th></tr>
    {% for customer in customers %}
    <tr>
        <td>{{ customer.id }}</td>
        <td>{{ customer.name }}</td>
        <td>{{ customer.phone }}</td>
        <td>{% if customer.discount_percent is not None %}VIP ({{ customer.discount_percent }}%){% else %}Zwykly{% endif %}</td>
    </tr>
    {% empty %}
    <tr><td colspan="4">Brak klientow</td></tr>
    {% endfor %}
</table>
{% endblock %}
```

Uwaga: `customer.discount_percent` istnieje tylko na VIPCustomer - dla zwyklego klienta sprawdzamy `is not None`.

**Krok 5:** Stworz template `customers_app/templates/customers_app/customer_form.html`:

```html
{% extends "base.html" %}

{% block title %}Dodaj klienta{% endblock %}

{% block content %}
<h1>Dodaj klienta</h1>

{% if errors %}
<div style="color: red;">
    {% for error in errors %}
    <p>{{ error }}</p>
    {% endfor %}
</div>
{% endif %}

<form method="post">
    {% csrf_token %}
    <div>
        <label>Imie:</label>
        <input type="text" name="name" value="{{ name }}" required>
    </div>
    <div>
        <label>Telefon:</label>
        <input type="text" name="phone" value="{{ phone }}" required>
    </div>
    <div>
        <label>Typ:</label>
        <select name="type">
            <option value="regular">Zwykly klient</option>
            <option value="vip">VIP</option>
        </select>
    </div>
    <div>
        <label>Rabat VIP (%):</label>
        <input type="number" name="discount" value="10" min="1" max="50">
        <small>(tylko dla VIP)</small>
    </div>
    <button type="submit">Dodaj</button>
</form>

<a href="/klienci/">Powrot do listy</a>
{% endblock %}
```

**Krok 6:** Sprawdz! Wejdz na /klienci/ - zobaczysz istniejacych klientow z pliku JSON. Dodaj nowego przez formularz.

---

## Czesc 6: Order Views (50 min)

### SHOW: Order list + detail

Kluczowa zlozonosc: zamowienia lacza klientow z pizzami.

```python
# orders_app/views.py
def order_list(request):
    orders_data = _load_orders()  # z pliku JSON
    # ... przygotuj dane do wyswietlenia ...
    return render(request, 'orders_app/order_list.html', {'orders': orders_display})

def order_detail(request, order_id):
    # Znajdz zamowienie, oblicz sumy, rabaty VIP
    return render(request, 'orders_app/order_detail.html', context)
```

### DO: Order list + detail views

Cel: zbuduj app do wyswietlania zamowien. Zamowienia sa zapisywane jako JSON - kazde zamowienie laczy klienta z pizzami.

**Krok 1:** Stworz nowy app:

```bash
python3 manage.py startapp orders_app
```

**WAZNE - 2 kroki konfiguracji (tak samo jak poprzednio):**

**A)** Dodaj `'orders_app'` do `INSTALLED_APPS` w `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'menu_app',
    'customers_app',
    'orders_app',    # <- DODAJ
]
```

**B)** Dodaj routing w glownym `pizzeria_project/urls.py`:

```python
urlpatterns = [
    path('menu/', include('menu_app.urls')),
    path('klienci/', include('customers_app.urls')),
    path('zamowienia/', include('orders_app.urls')),    # <- DODAJ
]
```

**Krok 2:** Stworz `orders_app/views.py` - zacznij od helperow do odczytu/zapisu zamowien:

```python
import os
import json
from django.shortcuts import render, redirect
from django.http import Http404
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.pizza import Menu
from rozwiazanie_weekend2.customer import CustomerManager
from rozwiazanie_weekend2.exceptions import CustomerNotFoundError, PizzaNotFoundError

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
```

Uwaga: zamowienia zapisujemy recznie przez `json.load/dump` bo nasz engine z Weekend 2 nie mial `OrderManager.save_to_file()`. To dobry przyklad jak laczyc istniejacy kod z nowym.

**Krok 3:** Dodaj view listy zamowien:

```python
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
```

**Krok 4:** Dodaj view szczegulow zamowienia:

```python
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
```

**Krok 5:** Stworz `orders_app/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
]
```

**Krok 6:** Stworz template `orders_app/templates/orders_app/order_list.html`:

```html
{% extends "base.html" %}

{% block title %}Zamowienia{% endblock %}

{% block content %}
<h1>Zamowienia</h1>

{% if orders %}
<table>
    <tr><th>#</th><th>Klient</th><th>Pozycje</th><th>Suma</th></tr>
    {% for order in orders %}
    <tr>
        <td><a href="/zamowienia/{{ order.id }}/">#{{ order.id }}</a></td>
        <td>{{ order.customer_name }} {% if order.is_vip %}(VIP){% endif %}</td>
        <td>{{ order.items_count }}</td>
        <td>{{ order.total }} zl</td>
    </tr>
    {% endfor %}
</table>
{% else %}
<p>Brak zamowien. <a href="/zamowienia/nowe/">Zloz pierwsze zamowienie</a></p>
{% endif %}
{% endblock %}
```

**Krok 7:** Stworz template `orders_app/templates/orders_app/order_detail.html`:

```html
{% extends "base.html" %}

{% block title %}Zamowienie #{{ order_id }}{% endblock %}

{% block content %}
<h1>Zamowienie #{{ order_id }}</h1>
<p>Klient: {{ customer_name }}</p>

<table>
    <tr><th>Pizza</th><th>Cena</th><th>Ilosc</th><th>Razem</th></tr>
    {% for item in items %}
    <tr>
        <td>{{ item.pizza_name }}</td>
        <td>{{ item.pizza_price }} zl</td>
        <td>{{ item.quantity }}</td>
        <td>{{ item.total }} zl</td>
    </tr>
    {% endfor %}
</table>

<p>Suma: {{ subtotal }} zl</p>
{% if discount_percent %}
<p>Rabat VIP ({{ discount_percent }}%): -{{ discount_amount }} zl</p>
{% endif %}
<p><strong>Do zaplaty: {{ total }} zl</strong></p>

<a href="/zamowienia/">Powrot do listy</a>
{% endblock %}
```

**Krok 8:** Na razie lista zamowien bedzie pusta (nie mamy jeszcze formularza tworzenia). To OK - formularz dodamy w nastepnym cwiczeniu.

---

## Czesc 7: Formularz zamowienia (40 min)

### SHOW: Formularz z select

```html
<form method="post">
    {% csrf_token %}
    <select name="customer_id">
        {% for customer in customers %}
        <option value="{{ customer.id }}">{{ customer.name }}</option>
        {% endfor %}
    </select>

    <select name="pizza_name">
        {% for pizza in pizzas %}
        <option value="{{ pizza.name }}">{{ pizza.name }} ({{ pizza.price }} zl)</option>
        {% endfor %}
    </select>
    <input type="number" name="quantity" min="1" value="1">

    <button type="submit">Zloz zamowienie</button>
</form>
```

### DO: Order creation form

Cel: stworz formularz na /zamowienia/nowe/ gdzie mozna wybrac klienta, pizze i ilosc.

**Krok 1:** Dodaj view `order_create` w `orders_app/views.py`:

```python
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
```

Zwroc uwage: view musi zaladowac liste klientow I liste pizz zeby wyswietlic je w formularz jako `<select>`.

**Krok 2:** Dodaj URL w `orders_app/urls.py`:

```python
urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('nowe/', views.order_create, name='order_create'),        # PRZED <int:order_id>
    path('<int:order_id>/', views.order_detail, name='order_detail'),
]
```

**Krok 3:** Stworz template `orders_app/templates/orders_app/order_form.html`:

```html
{% extends "base.html" %}

{% block title %}Nowe zamowienie{% endblock %}

{% block content %}
<h1>Zloz zamowienie</h1>

{% if errors %}
<div style="color: red;">
    {% for error in errors %}
    <p>{{ error }}</p>
    {% endfor %}
</div>
{% endif %}

<form method="post">
    {% csrf_token %}
    <div>
        <label>Klient:</label>
        <select name="customer_id" required>
            <option value="">-- Wybierz klienta --</option>
            {% for customer in customers %}
            <option value="{{ customer.id }}">{{ customer.name }}</option>
            {% endfor %}
        </select>
    </div>
    <div>
        <label>Pizza:</label>
        <select name="pizza_name" required>
            <option value="">-- Wybierz pizze --</option>
            {% for pizza in pizzas %}
            <option value="{{ pizza.name }}">{{ pizza.name }} ({{ pizza.price }} zl)</option>
            {% endfor %}
        </select>
    </div>
    <div>
        <label>Ilosc:</label>
        <input type="number" name="quantity" min="1" value="1" required>
    </div>
    <button type="submit">Zloz zamowienie</button>
</form>

<a href="/zamowienia/">Powrot do listy</a>
{% endblock %}
```

**Krok 4:** Sprawdz! Wejdz na /zamowienia/nowe/, wybierz klienta i pizze, zloz zamowienie. Po zlozeniu powinienes zobaczyc szczegoly zamowienia z suma. Jezeli wybrales klienta VIP - powinien byc naliczony rabat.

---

## Czesc 8: Django Messages + Finishing Touches (15 min)

### SHOW: Messages framework

```python
from django.contrib import messages

def pizza_add(request):
    if request.method == 'POST':
        # ... obsluga formularza ...
        messages.success(request, f"Dodano pizze: {name}")
        return redirect('pizza_list')
```

```html
<!-- base.html -->
{% if messages %}
{% for message in messages %}
<div class="alert alert-{{ message.tags }}">{{ message }}</div>
{% endfor %}
{% endif %}
```

---

## Czesc 9: Pelna integracja (25 min)

### DO: Przetestuj caly flow

1. Przegladaj menu (/menu/)
2. Dodaj nowa pizze (/menu/dodaj/)
3. Dodaj nowego klienta (/klienci/dodaj/)
4. Zloz zamowienie (/zamowienia/nowe/)
5. Zobacz szczegoly zamowienia
6. Sprawdz czy VIP rabat sie nalicza

---

## Czesc 10: Podsumowanie weekendu (10 min)

### Progresja kursu

```
Weekend 1: proceduralne -> OOP (klasy, dziedziczenie)
Weekend 2: wyjatki -> I/O (JSON) -> testy (pytest)
Weekend 3: Git -> Django (views, templates, forms)
Weekend 4: REST API -> wiecej Django
```

### Co zrobilismy dzisiaj:
- Git: kontrola wersji, branches, GitHub
- Django: views, templates, URL routing
- Formularze HTML + CSRF
- Pelna aplikacja webowa bez bazy danych!
- Integracja rozwiazanie_weekend2/ z Django

### Co dalej (Weekend 4):
- REST API z Django REST Framework
- JSON responses zamiast HTML
- Testowanie API
- Deployment
