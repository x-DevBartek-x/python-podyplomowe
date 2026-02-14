# Dzien 1: Git + Django Intro

## Czesc 1: Recap Weekend 1+2 (20 min)

### Co zrobilismy do tej pory

**Weekend 1:** Programowanie proceduralne -> OOP
- Klasy: Pizza, Menu, Customer, VIPCustomer, Order
- Dziedziczenie: Customer -> VIPCustomer
- Metody specjalne: __init__, __str__, __len__, __iter__

**Weekend 2:** Wyjatki + I/O + Testy
- Hierarchia wyjatkow: PizzeriaError -> ValidationError, NotFoundError, OperationError
- Serializacja JSON: to_dict(), from_dict(), save_to_file(), load_from_file()
- Testy pytest: fixtures, parametrize, pytest.raises

### Prezentacja rozwiazania

Pokazac `rozwiazanie_weekend2/`:
```bash
cd 1415-02-2026  # lub katalog nadrzedny wzgledem rozwiazanie_weekend2/
python3 -m rozwiazanie_weekend2.main
pytest rozwiazanie_weekend2/ -v
```

---

## Czesc 2: Git Fundamentals (40 min)

### Czym jest Git?

- System kontroli wersji (VCS)
- Sledzenie zmian w kodzie
- Cofanie bledow
- Wspolpraca w zespole

### Po co kontrola wersji?

**Bez Gita:**
```
projekt_v1/
projekt_v2_final/
projekt_v2_final_PRAWDZIWY/
projekt_v3_do_oddania/
```

**Z Gitem:**
```
projekt/          <- jeden folder, cala historia w .git/
```

### Podstawowe koncepcje

```
Working Directory  -->  Staging Area  -->  Repository
    (pliki)           (git add)        (git commit)
```

### SHOW: Podstawowe komendy (10 min)

```bash
# Inicjalizacja
mkdir demo-git
cd demo-git
git init

# Sprawdz status
git status

# Stworz plik
echo "Hello Git" > hello.txt
git status

# Dodaj do staging
git add hello.txt
git status

# Commit
git commit -m "Pierwszy commit"

# Historia
git log
git log --oneline
```

### SHOW: Branches (15 min)

```bash
# Stworz branch
git branch feature-x
git switch feature-x

# Zrob zmiany
echo "Nowa funkcja" > feature.txt
git add feature.txt
git commit -m "Dodaj nowa funkcje"

# Wroc na main
git switch main
ls  # feature.txt nie istnieje!

# Merge
git merge feature-x
ls  # feature.txt istnieje!
```

### SHOW: Merge conflict

```bash
# Na main
echo "cena: 25" > config.txt
git add config.txt && git commit -m "Cena 25"

# Branch A
git branch branch-a
git switch branch-a
echo "cena: 30" > config.txt
git add config.txt && git commit -m "Cena 30"

# Wroc na main, inna zmiana
git switch main
echo "cena: 28" > config.txt
git add config.txt && git commit -m "Cena 28"

# Merge - CONFLICT!
git merge branch-a
# Otworz config.txt - pokaz markery <<<<< ===== >>>>>
# Rozwiaz, git add, git commit
```

### Git Cheatsheet

```
PODSTAWY
  git init                    Inicjalizuj nowe repo w biezacym katalogu
  git status                  Pokaz stan plikow (zmodyfikowane, staged, untracked)
  git add <plik>              Dodaj plik do staging area
  git add .                   Dodaj wszystkie zmienione pliki
  git commit -m "wiadomosc"   Zapisz zmiany w historii
  git log --oneline           Pokaz skrocona historie commitow

BRANCHES
  git branch                  Lista branchow (* = aktualny)
  git branch <nazwa>          Stworz nowy branch
  git switch <nazwa>          Przelacz na branch
  git merge <nazwa>           Polacz branch do aktualnego

COFANIE
  git diff                    Pokaz niezacommitowane zmiany
  git restore <plik>          Cofnij zmiany w pliku (przed git add)
  git restore --staged <plik> Usun plik ze staging (cofnij git add)

REMOTE (GitHub)
  git clone <url>             Pobierz repo z GitHuba
  git push origin main        Wyslij commity na GitHuba
  git pull origin main        Pobierz zmiany z GitHuba

PRZYDATNE
  .gitignore                  Plik z lista plikow/katalogow do ignorowania
                              Python: __pycache__/, *.pyc, venv/, .env
```

---

## Czesc 3: GitHub (40 min)

### Czym jest GitHub?

- Hosting repozytoriow Git
- Wspolpraca: Pull Requests, Issues
- Fork = kopia repo na swoim koncie

### Fork vs Clone

- **Fork:** Kopia na GitHubie (Twoje konto)
- **Clone:** Kopia na komputerze (lokalna)
- **Typowy flow:** Fork -> Clone -> Commit -> Push

### SHOW: GitHub flow (15 min)

1. Pokaz jak zalozyc konto (screenshot/live)
2. Fork repozytorium kursu
3. Clone: `git clone https://github.com/USERNAME/python-podyplomowe.git`
4. Push: `git push origin main`

**WAZNE:** Uzyj HTTPS + Personal Access Token (nie SSH na warsztacie)

---

## Czesc 4: Django Intro (45 min)

### Czym jest web framework?

```
Klient (przegladarka)  <--->  Serwer (Django)
     HTTP Request      --->     View function
     HTTP Response     <---     HTML / JSON
```

### Django - "batteries included"

- URL routing
- Template engine
- ORM (my nie uzyje w tym weekendzie!)
- Admin panel
- Forms
- Authentication

### SHOW: Django od zera (15 min)

```bash
# Instalacja
pip install django

# Nowy projekt
django-admin startproject mojprojekt
cd mojprojekt

# Uruchom serwer
python manage.py runserver
# Otworz http://127.0.0.1:8000/
```

### Struktura projektu Django

```
mojprojekt/
├── manage.py           <- narzedzie CLI
├── mojprojekt/
│   ├── __init__.py
│   ├── settings.py     <- konfiguracja
│   ├── urls.py         <- routing URL
│   └── wsgi.py         <- WSGI entry point
```

**manage.py** - narzedzie do zarzadzania projektem z terminala:
- `python manage.py runserver` - uruchamia serwer deweloperski
- `python manage.py startapp menu_app` - tworzy nowy modul (app)
- `python manage.py check` - sprawdza czy konfiguracja jest poprawna

**settings.py** - cala konfiguracja projektu w jednym miejscu:
- `INSTALLED_APPS` - lista zainstalowanych modulow. **Jezeli Twoj app nie jest na liscie, Django go nie widzi!**
- `MIDDLEWARE` - warstwy posrednie przez ktore przechodzi kazdy request (ochrona CSRF, bezpieczenstwo)
- `TEMPLATES` - gdzie Django szuka szablonow HTML
- `STATIC_URL` - sciezka do plikow statycznych (CSS, JS, obrazki)
- `DEBUG = True` - tryb deweloperski (pokazuje ladne strony bledow)

**urls.py** - mapowanie URL na funkcje:
```python
# "Kiedy ktos wejdzie na /hello/, wywolaj funkcje views.hello"
path('hello/', views.hello)
```

**wsgi.py** - punkt wejscia dla serwera produkcyjnego.
WSGI (Web Server Gateway Interface) to standard Pythona - okresla jak serwer HTTP
(np. Apache, Gunicorn) komunikuje sie z aplikacja Django.
My uzywamy `manage.py runserver` (serwer deweloperski) wiec tego pliku nie ruszamy.

### Projekt vs App

- **Projekt** = cala aplikacja (np. "pizzeria online")
- **App** = wydzielony modul/funkcjonalnosc (np. "menu", "klienci", "zamowienia")
- Jeden projekt sklada sie z wielu appow
- Kazdy app ma swoje: views.py, urls.py, templates/

```
pizzeria_project/            <- PROJEKT (konfiguracja)
├── settings.py
├── urls.py                  <- glowny routing, deleguje do appow
menu_app/                    <- APP (funkcjonalnosc "menu")
├── views.py                 <- logika: co zwrocic
├── urls.py                  <- routing: jakie URLe obsluguje ten app
├── templates/menu_app/      <- szablony HTML
customers_app/               <- APP (funkcjonalnosc "klienci")
orders_app/                  <- APP (funkcjonalnosc "zamowienia")
```

### Cykl zycia requestu

```
Przegladarka: GET /menu/
        |
        v
    urls.py  -->  "menu/" pasuje do menu_app.urls
        |
        v
    menu_app/urls.py  -->  "" pasuje do views.pizza_list
        |
        v
    views.py: pizza_list(request)
        |   - laduje dane z JSON
        |   - przygotowuje kontekst
        v
    render('pizza_list.html', {'pizzas': [...]})
        |
        v
    Przegladarka: wyswietla strone HTML z lista pizz
```

---

## Czesc 5: Pierwszy view (30 min)

### SHOW: Hello World view (GENERIC - nie pizza!)

```python
# W dowolnym pliku, np. views.py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Witaj swiecie!")
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
]
```

### DO: Stworz projekt Django "pizzeria" + pierwszy view

Koniec pracy z `mojprojekt` - to bylo tylko demo. Teraz tworzymy **wlasciwy projekt kursu** w ktorym bedziemy budowac aplikacje pizzerii.

**Krok 1:** Stworz katalog i projekt Django:

```bash
cd 1415-02-2026    # katalog z rozwiazanie_weekend2/
mkdir pizzeria_django
cd pizzeria_django
django-admin startproject pizzeria_project .
```

**UWAGA:** Kropka `.` na koncu oznacza "stworz projekt W biezacym katalogu" (zamiast tworzyc kolejny podkatalog). Dzieki temu mamy:

```
pizzeria_django/
├── manage.py
└── pizzeria_project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

**Krok 2:** Sprawdz czy serwer dziala:

```bash
python3 manage.py runserver
```

Zignoruj warning o migracjach - nie uzywamy bazy danych. Wejdz na http://127.0.0.1:8000/ - powinienes zobaczyc strone powitalna Django.

**Krok 3:** Stworz plik `pizzeria_project/views.py` (obok urls.py) i napisz pierwszy view:

```python
# pizzeria_project/views.py
from django.http import HttpResponse

def witaj(request):
    return HttpResponse("Witaj w pizzerii!")
```

**Krok 4:** Podepnij URL w `pizzeria_project/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.witaj),
]
```

**Krok 5:** Sprawdz! Wejdz na http://127.0.0.1:8000/ - powinienes zobaczyc "Witaj w pizzerii!".

---

## Czesc 6: Templates (40 min)

### Gdzie trzymac szablony HTML?

Zanim zaczniemy uzywac szablonow, musimy powiedziec Django gdzie ich szukac.

**Krok 1:** Stworz katalog `templates/` **obok manage.py** (w katalogu glownym projektu):

```
mojprojekt/                  <- katalog GLOWNY projektu (tu uruchamiasz manage.py)
├── manage.py
├── mojprojekt/              <- paczka konfiguracyjna (ta sama nazwa - to normalne!)
│   ├── __init__.py
│   ├── settings.py          <- konfiguracja (tu zmieniasz DIRS)
│   ├── urls.py              <- routing URL (tu dodajesz path())
│   ├── views.py             <- STWORZ TEN PLIK! (domyslnie nie istnieje)
│   └── wsgi.py
└── templates/               <- STWORZ TEN KATALOG! Obok manage.py
    └── books/
        └── book_list.html
```

**UWAGA 1:** `django-admin startproject mojprojekt` tworzy katalog `mojprojekt/mojprojekt/` (podwojna nazwa). To jest normalne - zewnetrzny to katalog projektu, wewnetrzny to paczka konfiguracyjna Pythona.

**UWAGA 2:** Django NIE tworzy pliku `views.py` w paczce konfiguracyjnej - musisz go stworzyc sam. Katalog `templates/` tez nie istnieje domyslnie.

**Zasada:** Nowe pliki (`views.py`, `templates/`) tworz w odpowiednim miejscu:
- `views.py` -> wewnatrz paczki konfiguracyjnej (obok `urls.py` i `settings.py`)
- `templates/` -> w katalogu glownym (obok `manage.py`)

**Krok 2:** W `settings.py` powiedz Django zeby szukal w tym katalogu:

```python
# settings.py - znajdz sekcje TEMPLATES i zmien DIRS z [] na:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],    # <- DODAJ TO (domyslnie jest [])
        'APP_DIRS': True,
        ...
    },
]
```

`BASE_DIR` to sciezka do katalogu z `manage.py` - jest juz zdefiniowana na gorze `settings.py`.
`BASE_DIR / 'templates'` = szukaj szablonow w katalogu `templates/` obok `manage.py`.

Bez tej zmiany Django nie wie gdzie szukac szablonow i dostaniesz blad: **TemplateDoesNotExist**.

### SHOW: Template z kontekstem (GENERIC - lista ksiazek)

```python
# views.py
from django.shortcuts import render

def book_list(request):
    books = [
        {'title': 'Python Crash Course', 'author': 'Eric Matthes'},
        {'title': 'Fluent Python', 'author': 'Luciano Ramalho'},
    ]
    return render(request, 'books/book_list.html', {'books': books})
```

Stworz plik `templates/books/book_list.html`:

```html
<h1>Ksiazki</h1>
<ul>
{% for book in books %}
    <li>{{ book.title }} - {{ book.author }}</li>
{% empty %}
    <li>Brak ksiazek</li>
{% endfor %}
</ul>
```

### Template tags

- `{{ zmienna }}` - wyswietl wartosc
- `{% for item in lista %}` - petla
- `{% if warunek %}` - warunek
- `{% extends "base.html" %}` - dziedziczenie szablonow
- `{% block content %}` - blok do nadpisania

### DO: Integracja rozwiazanie_weekend2 z Django + pizza_list

Cel: podlaczyc nasz engine z Weekend 1+2 do projektu Django i wyswietlic liste pizz w przegladarce.

**Krok 1: Skopiuj engine do projektu Django**

Skopiuj caly katalog `rozwiazanie_weekend2/` do srodka `pizzeria_django/`:

```bash
cp -r ../rozwiazanie_weekend2 .
```

Teraz struktura powinna wygladac tak:

```
pizzeria_django/
├── manage.py
├── pizzeria_project/
└── rozwiazanie_weekend2/       <- kopia naszego engine z Weekend 1+2
    ├── __init__.py
    ├── pizza.py, customer.py, order.py, exceptions.py
    └── data/
        ├── menu.json
        └── customers.json
```

Dzieki temu Django widzi `rozwiazanie_weekend2` jako zwykly pakiet Pythona - zadna dodatkowa konfiguracja nie jest potrzebna.

**Krok 2: Sprawdz czy import dziala**

```bash
python3 manage.py shell
>>> from rozwiazanie_weekend2.pizza import Pizza, Menu
>>> from rozwiazanie_weekend2 import DATA_DIR
>>> print(DATA_DIR)  # powinno wskazywac na .../pizzeria_django/rozwiazanie_weekend2/data/
>>> exit()
```

**Krok 3: Stworz app menu_app**

Do tej pory pisalismy view bezposrednio w `pizzeria_project/views.py`. Teraz zaczynamy budowac wlasciwa strukture - kazda funkcjonalnosc w osobnym app:

```bash
python3 manage.py startapp menu_app
```

To stworzy katalog `menu_app/` z plikami: `views.py`, `__init__.py`, `apps.py`, itp.

Dodaj `'menu_app'` do `INSTALLED_APPS` w `pizzeria_project/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'menu_app',
]
```

**Krok 4: Napisz view pizza_list**

Otworz `menu_app/views.py` i zastap zawartosc:

```python
# menu_app/views.py
import os
from django.shortcuts import render
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.pizza import Menu

MENU_FILE = os.path.join(DATA_DIR, 'menu.json')

def pizza_list(request):
    menu = Menu()
    menu.load_from_file(MENU_FILE)
    return render(request, 'menu_app/pizza_list.html', {'pizzas': list(menu)})
```

Wyjasnienie importow:
- `from rozwiazanie_weekend2 import DATA_DIR` - sciezka do katalogu data/ z naszymi JSON-ami
- `from rozwiazanie_weekend2.pizza import Menu` - klasa Menu, ktora napisalismy na Weekend 1
- `os.path.join(DATA_DIR, 'menu.json')` - pelna sciezka do pliku z menu

**Krok 5: Stworz katalog na template i plik HTML**

Stworz katalog `menu_app/templates/menu_app/` (tak, podwojna nazwa - to konwencja Django):

```bash
mkdir -p menu_app/templates/menu_app
```

Dlaczego podwojna nazwa? Django szuka szablonow we **wszystkich** appach naraz. Gdyby dwa appy mialy plik `list.html`, Django nie wiedzialby ktory uzyc. Podkatalog z nazwa appa (`menu_app/`) dziala jak namespace - rozroznia szablony miedzy appami.

Stworz plik `menu_app/templates/menu_app/pizza_list.html`:

```html
<!DOCTYPE html>
<html>
<head><title>Menu Pizzerii</title></head>
<body>
    <h1>Menu Pizzerii</h1>
    <ul>
    {% for pizza in pizzas %}
        <li>{{ pizza.name }} - {{ pizza.price }} zl</li>
    {% empty %}
        <li>Brak pizz w menu</li>
    {% endfor %}
    </ul>
</body>
</html>
```

**Krok 6: Dodaj URL-e**

Stworz plik `menu_app/urls.py` (Django go nie tworzy automatycznie):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
]
```

Teraz podepnij app URL-e w glownym `pizzeria_project/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('menu/', include('menu_app.urls')),
]
```

`include('menu_app.urls')` oznacza: "wszystko co zaczyna sie od /menu/ deleguj do menu_app".

**Krok 7: Sprawdz!**

```bash
python3 manage.py runserver
```

Wejdz na http://127.0.0.1:8000/menu/ - powinienes zobaczyc liste pizz z pliku JSON.

Gratulacje - wlasnie podlaczyles swoj engine z Weekend 1+2 do Django!

---

## Podsumowanie dnia 1

### Co zrobilismy:
1. Git: init, add, commit, branch, merge
2. GitHub: fork, clone, push
3. Django: startproject, runserver
4. Pierwszy view + template
5. pizza_list z rozwiazanie_weekend2/

### Preview dnia 2:
- Detail views z parametrami URL
- Static files + Bootstrap
- Formularze HTML + POST
- Pelna aplikacja: menu + klienci + zamowienia
