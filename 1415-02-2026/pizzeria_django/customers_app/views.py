import os
from django.shortcuts import render, redirect
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.customer import Customer, VIPCustomer, CustomerManager
from django.contrib import messages

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
            messages.success(request, f"Dodano Klienta: {name}")
            return redirect('customer_list')

        return render(request, 'customers_app/customer_form.html', {
            'errors': errors,
            'name': name,
            'phone': phone,
        })

    return render(request, 'customers_app/customer_form.html')