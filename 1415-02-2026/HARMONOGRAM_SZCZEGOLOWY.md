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

### Blok 1 (8:30-10:30) - Views, Static Files, Forms - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 8:30-8:45 | 15 min | Recap dnia 1, weryfikacja ze Django dziala | Intro |
| 8:45-9:00 | 15 min | **SHOW:** Detail view z parametrem URL (GENERIC: ksiazka/<int:pk>) | Live coding |
| 9:00-9:15 | 15 min | **DO:** pizza_detail view z <str:name> | Cwiczenie |
| 9:15-9:20 | 5 min | **REVIEW:** Omowienie | Review |
| 9:20-9:35 | 15 min | **SHOW:** Static files + Bootstrap CDN + base.html (extends/block) | Live coding |
| 9:35-9:55 | 20 min | **DO:** Dodaj base.html z nawigacja, ostyluj pizza pages | Cwiczenie |
| 9:55-10:00 | 5 min | **REVIEW:** Ostylowana strona | Review |
| 10:00-10:15 | 15 min | **SHOW:** HTML forms + POST + CSRF + redirect (GENERIC: formularz kontaktowy) | Live coding |
| 10:15-10:25 | 10 min | **DO:** Formularz dodawania pizzy (name + price) | Cwiczenie |
| 10:25-10:30 | 5 min | **REVIEW:** Omowienie | Review |

### Przerwa (10:30-10:40) - 10 min

### Blok 2 (10:40-12:40) - Building Full App - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 10:40-10:55 | 15 min | **SHOW:** Obsluga bledow w views - try/except + user-friendly messages | Live coding |
| 10:55-11:10 | 15 min | **DO:** Error handling: PizzaNotFoundError->404, walidacja w formularzu | Cwiczenie |
| 11:10-11:15 | 5 min | **REVIEW:** Omowienie | Review |
| 11:15-11:30 | 15 min | **SHOW:** Customer views (lista + dodawanie, Customer vs VIPCustomer) | Live coding |
| 11:30-11:55 | 25 min | **DO:** Zbuduj customers_app: lista + formularz (wybor typu klienta) | Cwiczenie |
| 11:55-12:00 | 5 min | **REVIEW:** Customer views dzialaja | Review |
| 12:00-12:10 | 10 min | **SHOW:** Order views - zlozonosc: wybor klienta + wybor pizz | Live coding |
| 12:10-12:35 | 25 min | **DO:** Zbuduj orders_app: order_list + order_detail (pozycje + total + VIP rabat) | Cwiczenie |
| 12:35-12:40 | 5 min | Buffer / Q&A | Dyskusja |

### Przerwa obiadowa (12:40-13:10) - 30 min

### Blok 3 (13:10-15:00) - Order Flow + Integration - 110 min

| Czas | Czas trwania | Temat | Typ |
|------|-------------|-------|-----|
| 13:10-13:25 | 15 min | **SHOW:** Formularz zamowienia - select klienta, select pizz + ilosc | Live coding |
| 13:25-13:50 | 25 min | **DO:** Order creation form + POST handler | Cwiczenie |
| 13:50-13:55 | 5 min | **REVIEW:** Dzialajace tworzenie zamowien | Review |
| 13:55-14:10 | 15 min | **SHOW:** Django messages framework + finishing touches | Live coding |
| 14:10-14:35 | 25 min | **DO:** Pelna integracja - przetestuj caly flow: dodaj klienta -> przegladaj menu -> zloz zamowienie -> zobacz zamowienie | Cwiczenie |
| 14:35-14:40 | 5 min | **REVIEW:** Demo pelnego flow - wolontariusz screen share | Review |
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
| Detail view | Ksiazka /<int:pk>/ | Pizza detail /<str:name>/ |
| Forms | Formularz kontaktowy (name + email + message) | Formularz dodawania pizzy |
| Error handling | Ksiazka nie znaleziona -> custom error | PizzaNotFoundError -> 404 |
| Customer views | Live coding na pizza app (ten sam pattern) | Pelne customers_app |

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
