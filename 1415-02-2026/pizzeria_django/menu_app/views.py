import os
from django.http import Http404
from django.shortcuts import render, redirect
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.pizza import Menu, Pizza
from rozwiazanie_weekend2.exceptions import PizzaNotFoundError, InvalidPriceError, DuplicatePizzaError
from django.contrib import messages

MENU_FILE = os.path.join(DATA_DIR, 'menu.json')

def pizza_list(request):
    menu = Menu()
    menu.load_from_file(MENU_FILE)
    return render(request, 'menu_app/pizza_list.html', {'pizzas': list(menu)})

def pizza_detail(request, name):
    menu = Menu()
    menu.load_from_file(MENU_FILE)
    try:
        pizza = menu.find_pizza(name)
    except PizzaNotFoundError:
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
                pizza = Pizza(name, price)
                menu = Menu()
                menu.load_from_file(MENU_FILE)
                menu.add_pizza(pizza)
                menu.save_to_file(MENU_FILE)
                messages.success(request, f"Dodano pizze: {name}")
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