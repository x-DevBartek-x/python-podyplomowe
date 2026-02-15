# Weekend 3: Git + Django - Harmonogram szczegolowy

## Informacje ogolne

- **Daty:** 14-15 lutego 2026
- **Godziny:** 8:30 - 15:00 (kazdy dzien)
- **Temat:** Git (pol dnia) + Django frontend (1.5 dnia)
- **Wymagania wstepne:** Weekend 1 (OOP) + Weekend 2 (wyjatki + testy)

## Struktura dnia

- **Blok 1:** 8:30 - 10:30 (120 min)
- **Przerwa:** 10:30 - 10:40 (10 min)
- **Blok 2:** 10:40 - 12:40 (120 min)
- **Przerwa obiadowa:** 12:40 - 13:10 (30 min)
- **Blok 3:** 13:10 - 15:00 (110 min)

**Czas roboczy:** ~5h 50min / dzien

---

## DZIEN 1: Git (rano) + Django Intro (popoludnie)

### Blok 1 (8:30-10:30) - Git Fundamentals - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 8:30-8:50 | 20 min | Powitanie, recap Weekend 1+2, prezentacja rozwiazanie_weekend2/ | Intro |
| 8:50-9:10 | 20 min | Teoria: Czym jest Git, po co kontrola wersji | Wyklad |
| 9:10-9:20 | 10 min | **SHOW:** git init, add, commit, status, log | Live coding |
| 9:20-9:40 | 20 min | **DO:** Zainicjalizuj repo, stworz pliki, zrob commity | Cwiczenie |
| 9:40-9:50 | 10 min | **REVIEW:** Omowienie + .gitignore (Python: __pycache__, .pyc, venv/) | Review |
| 9:50-10:05 | 15 min | **SHOW:** Branches - branch, switch, merge, merge conflict | Live coding |
| 10:05-10:25 | 20 min | **DO:** Stworz branch, zrob zmiany, merge, rozwiaz konflikt | Cwiczenie |
| 10:25-10:30 | 5 min | **REVIEW:** Omowienie merge conflicts | Review |

### Przerwa (10:30-10:40) - 10 min

### Blok 2 (10:40-12:40) - GitHub + Django Setup - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 10:40-11:00 | 20 min | Teoria: GitHub, remote repos, fork vs clone | Wyklad |
| 11:00-11:15 | 15 min | **SHOW:** Zalozenie konta GitHub + clone + push (HTTPS token) | Demo |
| 11:15-11:50 | 35 min | **DO:** Zaloz konto GitHub, fork python-podyplomowe, clone, push commit | Cwiczenie |
| 11:50-12:00 | 10 min | **REVIEW:** Weryfikacja - wszyscy maja fork + clone | Review |
| 12:00-12:20 | 20 min | Teoria: Czym jest web framework, HTTP request/response, klient-serwer | Wyklad |
| 12:20-12:35 | 15 min | **SHOW:** `pip install django`, `django-admin startproject`, runserver | Live coding |
| 12:35-12:40 | 5 min | Buffer / Q&A | Dyskusja |

### Przerwa obiadowa (12:40-13:10) - 30 min

### Blok 3 (13:10-15:00) - Django Views + Templates - 110 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 13:10-13:25 | 15 min | Teoria: Struktura projektu Django, apps, settings.py, URL routing | Wyklad |
| 13:25-13:40 | 15 min | **SHOW:** Pierwszy view "hello world" + urls.py (GENERIC: nie pizza) | Live coding |
| 13:40-13:55 | 15 min | **DO:** Stworz view "Witaj w pizzerii!" + podepnij URL | Cwiczenie |
| 13:55-14:00 | 5 min | **REVIEW:** Omowienie | Review |
| 14:00-14:15 | 15 min | **SHOW:** Templates - render(), zmienne, if/for, extends/block (GENERIC: lista ksiazek) | Live coding |
| 14:15-14:40 | 25 min | **DO:** Stworz menu_app, pizza_list view + template z danymi z rozwiazanie_weekend2/ | Cwiczenie |
| 14:40-14:50 | 10 min | **REVIEW:** Pizza list dziala w przegladarce! | Review |
| 14:50-14:55 | 5 min | Podsumowanie dnia. Preview dnia 2. | Outro |
| 14:55-15:00 | 5 min | "Zcommitujcie i pushujcie na forka!" | Cwiczenie |

---

## DZIEN 2: Django Full Day

### Blok 1 (8:30-10:30) - Detail Views, Static Files, Formularze - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 8:30-8:50 | 20 min | Recap dnia 1, sprawdzenie srodowiska, plan dnia 2 | Intro |
| 8:50-9:05 | 15 min | Teoria: Parametry URL (`<str:name>`, `<int:pk>`) + Http404 | Wyklad |
| 9:05-9:20 | 15 min | **SHOW:** Detail view (GENERIC: ksiazka/`<int:pk>`) + Http404 | Live coding |
| 9:20-9:35 | 15 min | **DO:** Cw. 1: pizza_detail z `<str:name>` + PizzaNotFoundError->404 | Cwiczenie |
| 9:35-9:50 | 15 min | Teoria: Dziedziczenie szablonow (extends/block) + static files + base.html | Wyklad |
| 9:50-10:00 | 10 min | **DO:** Cw. 2: Ostyluj pizza pages z base.html (extends/block) | Cwiczenie |
| 10:00-10:15 | 15 min | Teoria: HTTP GET vs POST, CSRF, POST-Redirect-GET, wzorzec formularza | Wyklad |
| 10:15-10:25 | 10 min | **SHOW:** Formularz kontaktowy (GENERIC) + `{% csrf_token %}` | Live coding |
| 10:25-10:30 | 5 min | Buffer / Q&A | Dyskusja |

### Przerwa (10:30-10:40) - 10 min

### Blok 2 (10:40-12:40) - Formularz pizzy + customers_app + orders_app - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 10:40-11:05 | 25 min | **DO:** Cw. 3: Formularz dodawania pizzy (POST, walidacja, try/except) | Cwiczenie |
| 11:05-11:15 | 10 min | **REVIEW:** Formularze - CSRF, kolejnosc URL, obsluga wyjatkow | Review |
| 11:15-11:20 | 5 min | Teoria: Budowanie kolejnego appa (wzorzec: startapp -> INSTALLED_APPS -> urls.py) | Wyklad |
| 11:20-11:35 | 15 min | **SHOW:** Customer views - `<select>` typ klienta, Customer vs VIPCustomer | Live coding |
| 11:35-12:00 | 25 min | **DO:** Cw. 4: Pelne customers_app od zera (lista + formularz z wyborem typu) | Cwiczenie |
| 12:00-12:05 | 5 min | Teoria: Zamowienia - zlozonosc, laczenie danych z dwoch zrodel, JSON | Wyklad |
| 12:05-12:15 | 10 min | **SHOW:** Order views - helpery JSON, przygotowanie danych pod template | Live coding |
| 12:15-12:40 | 25 min | **DO:** Cw. 5: orders_app lista + detail (`<int:order_id>`) | Cwiczenie |

### Przerwa obiadowa (12:40-13:10) - 30 min

### Blok 3 (13:10-15:00) - Formularz zamowien, Messages, Integracja - 110 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 13:10-13:20 | 10 min | Teoria: Formularz z danymi z wielu zrodel (`<select>` z JSON) | Wyklad |
| 13:20-13:30 | 10 min | **SHOW:** Order form - select klienta/pizzy, redirect z parametrem | Live coding |
| 13:30-13:55 | 25 min | **DO:** Cw. 6: Formularz zamowienia (/zamowienia/nowe/) | Cwiczenie |
| 13:55-14:05 | 10 min | **SHOW:** Django messages framework - messages.success(), typy, base.html | Live coding |
| 14:05-14:10 | 5 min | **DO:** Cw. 7: Dodaj messages.success() do pizza_add, customer_add, order_create | Cwiczenie |
| 14:10-14:30 | 20 min | **DO:** Cw. 8: Test end-to-end pelnej aplikacji (menu + klienci + zamowienia + bledy) | Cwiczenie |
| 14:30-14:40 | 10 min | **REVIEW:** Demo pelnego flow - wolontariusz screen share | Review |
| 14:40-14:50 | 10 min | Podsumowanie weekendu. Progresja: proceduralne->OOP->wyjatki->testy->git->web. Preview: REST API. | Wyklad |
| 14:50-14:55 | 5 min | "Commit + push na forka!" | Cwiczenie |
| 14:55-15:00 | 5 min | Q&A, pozegnanie | Outro |

---

## Przyklady SHOW vs DO

Zgodnie z ustalonym wzorcem: SHOW uzywa innej domeny niz DO.

| Sekcja | SHOW (przyklad) | DO (zadanie) |
|--------|----------------|--------------|
| Pierwszy view | "Witaj swiecie!" HttpResponse | "Witaj w pizzerii!" |
| Templates | Lista ksiazek ({% for book in books %}) | Pizza list z rozwiazanie_weekend2/ |
| Detail view + Http404 | Ksiazka /`<int:pk>`/ + Http404 | Pizza detail /`<str:name>`/ + PizzaNotFoundError->404 |
| Static files + base.html | Przegladnij base.html w szkielecie | Ostyluj pizza pages (extends/block) |
| Forms + POST | Formularz kontaktowy (name + email + message) | Formularz dodawania pizzy (walidacja + wyjatki) |
| Customer views | `<select>` typ klienta, Customer vs VIPCustomer | Pelne customers_app od zera |
| Order views | Helpery JSON, orders_display | orders_app lista + detail |
| Order form | `<select>` z wielu zrodel (klienci + pizze) | Formularz zamowienia |
| Messages | messages.success() | Dodaj messages do wszystkich views |

---

## Struktura URL

```
/                              -> redirect to /menu/
/menu/                         -> pizza_list
/menu/<str:name>/              -> pizza_detail
/menu/dodaj/                   -> pizza_add (GET: form, POST: create)
/klienci/                      -> customer_list
/klienci/dodaj/                -> customer_add
/zamowienia/                   -> order_list
/zamowienia/<int:order_id>/    -> order_detail
/zamowienia/nowe/              -> order_create
```

---

## Kluczowe decyzje architektoniczne

### Django BEZ ORM
- **Brak models.py** (brak modeli Django)
- **Brak migracji** (brak bazy danych)
- **Brak Django Admin** (wymaga modeli)
- Views importuja bezposrednio klasy z rozwiazanie_weekend2/ (Pizza, Menu, Customer, Order)
- Dane przechowywane w plikach JSON przez istniejace save_to_file/load_from_file
- `DATABASES = {}` (puste - brak bazy danych, brak warningow o migracjach)

### Pakiet rozwiazanie_weekend2/
- Ten sam kod co studenci wytworzyli na Weekend 1+2, skopiowany do srodka projektu Django
- Studenci kopiuja `rozwiazanie_weekend2/` do `pizzeria_django/` komenda `cp -r`
- Dzieki temu importy dzialaja bez dodatkowej konfiguracji (zadnych zmian w manage.py)
- rozwiazanie_weekend2/__init__.py eksportuje DATA_DIR
- Views rozwiazuja sciezki: MENU_FILE = os.path.join(DATA_DIR, 'menu.json')

### Obsluga formularzy
- Zwykle HTML <form> z {% csrf_token %} - BEZ modulu Django Forms
- Views przetwarzaja request.POST bezposrednio
- Istniejaca hierarchia wyjatkow zapewnia walidacje
