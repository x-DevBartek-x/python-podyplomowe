# Harmonogram szczegolowy - Weekend 2: Wyjatki, I/O, Testowanie

## Podsumowanie

| Dzien | Temat | Czas roboczy |
|-------|-------|--------------||
| **Dzien 1** | Obsluga wyjatkow i I/O | 5h 50min |
| **Dzien 2** | Testowanie i Debugowanie | 5h 50min |

---

## DZIEN 1: Obsluga wyjatkow i I/O (8:30 - 15:00)

### Blok 1 (8:30 - 10:30) - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|--------------|-------|-----|
| 8:30 - 8:50 | 20 min | Powitanie, recap Weekendu 1, setup check | Intro |
| 8:50 - 9:20 | 30 min | Teoria: Wyjatki w Pythonie | Wyklad |
| 9:20 - 9:30 | 10 min | **SHOW:** Przechwytywanie wyjatkow | Live coding |
| 9:30 - 9:45 | 15 min | **DO:** Zadanie samodzielne safe_operations | Cwiczenie |
| 9:45 - 9:50 | 5 min | **REVIEW:** Omowienie rozwiazan | Review |
| 9:50 - 10:05 | 15 min | **SHOW:** Rzucanie wyjatkow (raise) | Live coding |
| 10:05 - 10:25 | 20 min | **DO:** Walidacja w klasie Pizza | Cwiczenie |
| 10:25 - 10:30 | 5 min | **REVIEW:** Omowienie | Review |

### Przerwa (10:30 - 10:40) - 10 min

### Blok 2 (10:40 - 12:40) - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|--------------|-------|-----|
| 10:40 - 10:55 | 15 min | **SHOW:** Wlasne wyjatki (exceptions.py) | Live coding |
| 10:55 - 11:15 | 20 min | **DO:** Hierarchia wyjatkow | Cwiczenie |
| 11:15 - 11:20 | 5 min | **REVIEW:** Omowienie hierarchii | Review |
| 11:20 - 11:35 | 15 min | **SHOW:** Integracja wyjatkow z klasami | Live coding |
| 11:35 - 11:55 | 20 min | **DO:** Integracja z customer.py i order.py | Cwiczenie |
| 11:55 - 12:00 | 5 min | **REVIEW:** Omowienie | Review |
| 12:00 - 12:35 | 35 min | **DO:** Refaktoryzacja - pelna obsluga wyjatkow | Cwiczenie |
| 12:35 - 12:40 | 5 min | Buffer / Q&A | Dyskusja |

### Przerwa obiadowa (12:40 - 13:10) - 30 min

### Blok 3 (13:10 - 15:00) - 110 min

| Czas | Czas trwania | Temat | Typ |
|------|--------------|-------|-----|
| 13:10 - 13:25 | 15 min | Teoria: Praca z plikami i JSON | Wyklad |
| 13:25 - 13:40 | 15 min | Demo: open(), read(), write(), json | Demo |
| 13:40 - 13:50 | 10 min | **SHOW:** Funkcje I/O | Live coding |
| 13:50 - 14:05 | 15 min | **DO:** save/load dla slownikow | Cwiczenie |
| 14:05 - 14:10 | 5 min | **REVIEW:** Omowienie | Review |
| 14:10 - 14:25 | 15 min | **SHOW:** Serializacja obiektow (to_dict/from_dict) | Live coding |
| 14:25 - 14:35 | 10 min | **DO:** Serializacja Customer | Cwiczenie |
| 14:35 - 14:40 | 5 min | **REVIEW:** Omowienie | Review |
| 14:40 - 14:52 | 12 min | **DO:** Integracja persystencji w main.py | Cwiczenie |
| 14:52 - 14:55 | 3 min | Podsumowanie dnia | Wyklad |
| 14:55 - 15:00 | 5 min | Q&A, przygotowanie na jutro (pytest) | Outro |

---

## DZIEN 2: Testowanie i Debugowanie (8:30 - 15:00)

### Blok 1 (8:30 - 10:30) - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|--------------|-------|-----|
| 8:30 - 8:50 | 20 min | Powitanie, recap dnia 1, setup pytest | Intro |
| 8:50 - 9:20 | 30 min | Teoria: Testowanie, piramida testow, konwencje | Wyklad |
| 9:20 - 9:30 | 10 min | **SHOW:** Pierwszy test z pytest | Live coding |
| 9:30 - 9:45 | 15 min | **DO:** Testy dla Pizza | Cwiczenie |
| 9:45 - 9:50 | 5 min | **REVIEW:** Omowienie | Review |
| 9:50 - 10:05 | 15 min | **SHOW:** Testowanie wyjatkow (pytest.raises) | Live coding |
| 10:05 - 10:25 | 20 min | **DO:** Testy wyjatkow | Cwiczenie |
| 10:25 - 10:30 | 5 min | **REVIEW:** Omowienie | Review |

### Przerwa (10:30 - 10:40) - 10 min

### Blok 2 (10:40 - 12:40) - 120 min

| Czas | Czas trwania | Temat | Typ |
|------|--------------|-------|-----|
| 10:40 - 10:55 | 15 min | **SHOW:** Fixtures w pytest (conftest.py) | Live coding |
| 10:55 - 11:05 | 10 min | **DO:** Wlasne fixtures | Cwiczenie |
| 11:05 - 11:10 | 5 min | **REVIEW:** Omowienie fixtures | Review |
| 11:10 - 11:25 | 15 min | **SHOW:** Klasy testowe | Live coding |
| 11:25 - 11:45 | 20 min | **DO:** test_customer.py z klasami | Cwiczenie |
| 11:45 - 11:50 | 5 min | **REVIEW:** Omowienie | Review |
| 11:50 - 12:35 | 45 min | **DO:** Pelny zestaw testow | Cwiczenie |
| 12:35 - 12:40 | 5 min | Buffer / Q&A | Dyskusja |

### Przerwa obiadowa (12:40 - 13:10) - 30 min

### Blok 3 (13:10 - 15:00) - 110 min

| Czas | Czas trwania | Temat | Typ |
|------|--------------|-------|-----|
| 13:10 - 13:25 | 15 min | Teoria: Debugowanie, po co debugger? | Wyklad |
| 13:25 - 13:40 | 15 min | Demo: pdb - komendy i uzycie | Demo |
| 13:40 - 13:55 | 15 min | **SHOW:** Debugowanie z breakpoint() | Live coding |
| 13:55 - 14:05 | 10 min | **DO:** Debugowanie z pdb | Cwiczenie |
| 14:05 - 14:10 | 5 min | **REVIEW:** Omowienie | Review |
| 14:10 - 14:25 | 15 min | **SHOW:** Debugowanie w IDE (PyCharm/VS Code) | Live coding |
| 14:25 - 14:35 | 10 min | **DO:** Debugowanie w IDE | Cwiczenie |
| 14:35 - 14:40 | 5 min | **REVIEW:** Omowienie | Review |
| 14:40 - 14:50 | 10 min | Demo: Testy integracyjne i E2E | Demo |
| 14:50 - 14:55 | 5 min | Podsumowanie kursu (Weekend 1 + 2) | Wyklad |
| 14:55 - 15:00 | 5 min | Q&A, co dalej, pozegnanie | Outro |

---

## Legenda typow aktywnosci

| Typ | Opis | Kto aktywny |
|-----|------|-------------|
| **Intro/Outro** | Powitanie, pozegnanie, organizacja | Prowadzacy |
| **Wyklad** | Teoria, slajdy, wyjasnienia | Prowadzacy |
| **Demo** | Demonstracja w REPL/edytorze | Prowadzacy |
| **Live coding** | Kodowanie na zywo z narracja | Prowadzacy |
| **Cwiczenie** | Samodzielna praca studentow | Studenci |
| **Review** | Omowienie rozwiazan, Q&A | Wszyscy |
| **Dyskusja** | Pytania, problemy, buffer | Wszyscy |

---

## Checkpointy

### Dzien 1
- [ ] 9:50 - Wszyscy rozumieja try/except i raise?
- [ ] 11:20 - Wszyscy maja hierarchie wyjatkow?
- [ ] 12:40 - Wszyscy maja zintegrowane wyjatki?
- [ ] 14:55 - Wszyscy maja dzialajaca persystencje?

### Dzien 2
- [ ] 9:50 - Wszyscy uruchomili pierwszy test?
- [ ] 11:10 - Wszyscy rozumieja fixtures?
- [ ] 12:40 - Wszyscy maja zestaw testow?
- [ ] 14:40 - Wszyscy uzyli debuggera?

---

## Czas na poszczegolne aktywnosci

| Aktywnosc | Dzien 1 | Dzien 2 | Razem |
|-----------|---------|---------|-------|
| Intro/Outro | 25 min | 25 min | 50 min |
| Wyklad | 48 min | 50 min | 98 min |
| Demo | 15 min | 25 min | 40 min |
| Live coding | 70 min | 70 min | 140 min |
| Cwiczenie | 127 min | 130 min | 257 min |
| Review | 30 min | 30 min | 60 min |
| Dyskusja/Buffer | 35 min | 20 min | 55 min |
| **Razem roboczy** | **350 min** | **350 min** | **700 min** |
| Przerwy | 40 min | 40 min | 80 min |
| **Razem** | **390 min** | **390 min** | **780 min** |

---

## Zaleznosci od Weekendu 1

Weekend 2 zaklada, ze studenci:
1. Znaja klasy i obiekty (Pizza, Menu, Customer, Order)
2. Rozumieja dziedziczenie (VIPCustomer)
3. Maja dzialajacy kod z `baza_startowa/`

Jesli ktos nie byl na Weekendzie 1, daj mu `baza_startowa/` i krotkie wprowadzenie (5-10 min przed zajęciami).
