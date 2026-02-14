# Cwiczenie: Git od podstaw

## Czesc 1: Pierwsze repozytorium (20 min)

### Krok 1: Inicjalizacja
```bash
mkdir moja-pizzeria
cd moja-pizzeria
git init
```

### Krok 2: Pierwszy plik i commit
Stworz plik `menu.txt`:
```
MENU PIZZERII
=============
1. Margherita - 25 zl
2. Pepperoni - 30 zl
```

```bash
git add menu.txt
git commit -m "Dodaj menu pizzerii"
```

### Krok 3: Sprawdz status
```bash
git status
git log
```

### Krok 4: Kolejne zmiany
Dodaj do `menu.txt` nowa pizze:
```
3. Hawajska - 32 zl
```

Stworz plik `kontakt.txt`:
```
Pizzeria "U Studenta"
Tel: 123-456-789
```

```bash
git add menu.txt kontakt.txt
git commit -m "Dodaj Hawajska do menu i plik kontaktowy"
```

### Krok 5: .gitignore
Stworz plik `.gitignore`:
```
__pycache__/
*.pyc
.env
venv/
```

```bash
git add .gitignore
git commit -m "Dodaj .gitignore"
```

### Krok 6: Sprawdz historie
```bash
git log --oneline
```

Powinienes widziec 3 commity.

---

## Czesc 2: Branches i merge (20 min)

### Krok 1: Nowy branch
```bash
git branch nowe-pizze
git switch nowe-pizze
```

### Krok 2: Zmiany na branchu
Dodaj do `menu.txt`:
```
4. Quattro Formaggi - 35 zl
5. Capricciosa - 33 zl
```

```bash
git add menu.txt
git commit -m "Dodaj nowe pizze do menu"
```

### Krok 3: Wroc na main i zrob inna zmiane
```bash
git switch main
```

Zmien cene Margherity w `menu.txt` na 28 zl.

```bash
git add menu.txt
git commit -m "Podwyzka ceny Margherity"
```

### Krok 4: Merge
```bash
git merge nowe-pizze
```

Jesli nie ma konfliktu - merge powinien przejsc automatycznie (zmiany w roznych liniach).

### Krok 5: Sprowokuj conflict (opcjonalnie)
Na nowym branchu zmien cene Pepperoni na 35 zl.
Na main zmien cene Pepperoni na 32 zl.
Sprobuj merge - rozwiaz konflikt recznie.

```bash
git branch zmiana-ceny
git switch zmiana-ceny
# edytuj menu.txt - Pepperoni na 35
git add menu.txt && git commit -m "Pepperoni 35 zl"

git switch main
# edytuj menu.txt - Pepperoni na 32
git add menu.txt && git commit -m "Pepperoni 32 zl"

git merge zmiana-ceny
# CONFLICT! Otworz plik, rozwiaz recznie, potem:
git add menu.txt
git commit -m "Rozwiazanie konfliktu ceny Pepperoni"
```

---

## Czesc 3: GitHub (35 min)

### Krok 1: Zaloz konto na GitHub
Wejdz na https://github.com i zaloz konto (jesli nie masz).

### Krok 2: Fork repozytorium kursu
1. Wejdz na: `https://github.com/makspiechota/python-podyplomowe`
2. Kliknij **Fork** (prawy gorny rog)
3. Poczekaj az fork sie utworzy

### Krok 3: Clone swojego forka
```bash
cd ~/Desktop  # lub inny katalog
git clone https://github.com/TWOJ-USERNAME/python-podyplomowe.git
cd python-podyplomowe
```

### Krok 4: Sprawdz strukture
```bash
ls
git log --oneline -5
git remote -v
```

### Krok 5: Zrob zmiane i push
Stworz plik `studenci/TWOJE_IMIE.txt` z krotkim opisem.

```bash
git add studenci/
git commit -m "Dodaj mojego studenta"
git push origin main
```

### Krok 6: Sprawdz na GitHubie
Wejdz na swoj fork w przegladarce - powinienes widziec nowy commit.

---

## Podsumowanie komend

| Komenda | Opis |
|---------|------|
| `git init` | Inicjalizuj nowe repo |
| `git status` | Sprawdz stan plikow |
| `git add <plik>` | Dodaj plik do staging |
| `git commit -m "msg"` | Zatwierdz zmiany |
| `git log` | Historia commitow |
| `git log --oneline` | Krotka historia |
| `git branch <nazwa>` | Stworz branch |
| `git switch <nazwa>` | Przejdz na branch |
| `git merge <nazwa>` | Polacz branch |
| `git clone <url>` | Sklonuj repo |
| `git push origin main` | Wyslij na remote |
| `git pull` | Pobierz z remote |
