import os
from django.http import Http404
from django.shortcuts import render, redirect
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.pizza import Menu, Pizza
from rozwiazanie_weekend2.exceptions import PizzaNotFoundError, InvalidPriceError, DuplicatePizzaError
from django.contrib import messages
from django.shortcuts import render
from .models import Pizza
from django.core.exceptions import ValidationError
from django.db import IntegrityError

MENU_FILE = os.path.join(DATA_DIR, 'menu.json')

# def pizza_list(request):
#     menu = Menu()
#     menu.load_from_file(MENU_FILE)
#     return render(request, 'menu_app/pizza_list.html', {'pizzas': list(menu)})

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu_app/pizza_list.html', {'pizzas': pizzas})

def pizza_detail(request, name):
    pizzas = Pizza.objects.all()
    try:
        pizza = Pizza.objects.get(name=name)
    except Pizza.DoesNotExist:
        raise Http404(f"Pizza '{name}' nie znaleziona")
    return render(request, 'menu_app/pizza_detail.html', {'pizza': pizza})

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
                Pizza.objects.create(name=name, price=price)
                messages.success(request, f"Dodano pizzę: {name}")
                return redirect('pizza_list')
            except (ValueError, TypeError):
                errors.append("Nieprawidlowa cena.")
            except ValidationError as e:
                errors.extend(e.messages)
            except IntegrityError:
                errors.append(f"Pizza '{name}' juz istnieje!")

        return render(request, 'menu_app/pizza_form.html', {
            'errors': errors,
            'name': name,
            'price': price_str,
        })

    return render(request, 'menu_app/pizza_form.html')