from storage import zapisz_transakcje
from datetime import datetime


def pobierz_kwote():

    while True:
        try:
            kwota = float(input("Podaj kwote: "))
            if kwota <= 0:
                print("Kwota musi byc wieksza od zera.")
                continue
            return kwota
        except ValueError:
            print("Nieprawidlowa kwota.") 


def dodaj_przychod(transakcje):

    kwota = pobierz_kwote()
    kategoria = input("Podaj kategorie: ")
    opis = input("Podaj opis: ")

    slownik_transakcji = {
        "typ": "przychod",
        "kwota": kwota,
        "kategoria": kategoria,
        "opis": opis,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    transakcje.append(slownik_transakcji)
    if zapisz_transakcje(transakcje):
        print(f"Przychod {kwota:.2f} PLN zostal dodany.")
    else:
        transakcje.pop()
        print("Nie udalo sie zapisac zmian.")


def dodaj_wydatek(transakcje):

    kwota = pobierz_kwote()
    kategoria = input("Podaj kategorie: ")
    opis = input("Podaj opis: ")

    slownik_transakcji = {
        "typ": "wydatek",
        "kwota": kwota,
        "kategoria": kategoria,
        "opis": opis,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    transakcje.append(slownik_transakcji)
    if zapisz_transakcje(transakcje):
        print(f"Wydatek {kwota:.2f} PLN zostal dodany.")
    else:
        transakcje.pop()
        print("Nie udalo sie zapisac zmian.")


def usun_transakcje(transakcje):

    print("==== USUWANIE TRANSAKCJI ====")

    if not transakcje:
        print("Brak transakcji.")
        return

    for numer, transakcja in enumerate(transakcje, start=1):
        print(f"{numer}. [{transakcja['typ'].upper()}] {transakcja['kwota']:.2f} PLN | {transakcja['kategoria']} | {transakcja['opis']}")

    try:
        numer_do_usuniecia = int(input("Podaj numer transakcji do usuniecia: "))
    except ValueError:
        print("Nieprawidlowy numer transakcji.")
        return

    if numer_do_usuniecia < 1 or numer_do_usuniecia > len(transakcje):
        print("Nieprawidlowy numer transakcji.")
        return

    indeks_listy = numer_do_usuniecia - 1

    potwierdzenie = input("Czy na pewno usunac transakcje? (t/n): ").strip().lower()

    if potwierdzenie == "t":
        usunieta_transakcja = transakcje.pop(indeks_listy)
        if zapisz_transakcje(transakcje):
            print("Transakcja zostala usunieta.")
        else:
            transakcje.insert(indeks_listy, usunieta_transakcja)
            print("Nie udalo sie usunac transakcji.")
    elif potwierdzenie == "n":
        print("Anulowano usuwanie.")
    else:
        print("Nieprawidlowy wybor (t/n).")


def edytuj_transakcje(transakcje):

    print("==== EDYCJA TRANSAKCJI ====")

    if not transakcje:
        print("Brak transakcji.")
        return

    for numer, transakcja in enumerate(transakcje, start=1):
        print(f"{numer}. [{transakcja['typ'].upper()}] {transakcja['kwota']:.2f} PLN | {transakcja['kategoria']} | {transakcja['opis']}")

    try:
        numer_transakcji = int(input("Podaj numer transakcji do edycji: "))
    except ValueError:
        print("Nieprawidlowy numer transakcji.")
        return

    if numer_transakcji < 1 or numer_transakcji > len(transakcje):
        print("Nieprawidlowy numer transakcji.")
        return

    indeks_transakcji = numer_transakcji - 1

    print("Co chcesz zmienic?\n")
    print("""
    1. Kwote
    2. Kategorie
    3. Opis
    4. Anuluj
    """)

    try:
        opcja = int(input("Wybierz opcje: "))
    except ValueError:
        print("Nieprawidlowa opcja.")
        return

    if opcja < 1 or opcja > 4:
        print("Nieprawidlowa opcja.")
        return
   
    if opcja == 4:
        print("Anulowano edycje.")
        return

    if opcja == 1:
        stara_kwota = transakcje[indeks_transakcji]["kwota"]
        nowa_kwota = pobierz_kwote()
        transakcje[indeks_transakcji]["kwota"] = nowa_kwota
        if zapisz_transakcje(transakcje):
            print("Kwota zostala zmieniona.")
        else:
            transakcje[indeks_transakcji]["kwota"] = stara_kwota
            print("Nie udalo sie zmienic kwoty.")
    elif opcja == 2:
        stara_kategoria = transakcje[indeks_transakcji]["kategoria"]
        nowa_kategoria = input("Podaj nowa kategorie: ").strip()
        if not nowa_kategoria:
            print("Nieprawidlowe dane.")
            return
        transakcje[indeks_transakcji]["kategoria"] = nowa_kategoria
        if zapisz_transakcje(transakcje):
            print("Kategoria zostala zmieniona.")
        else:
            transakcje[indeks_transakcji]["kategoria"] = stara_kategoria
            print("Nie udalo sie zmienic kategorii.")
    elif opcja == 3:
        stary_opis = transakcje[indeks_transakcji]["opis"]
        nowy_opis = input("Podaj nowy opis: ").strip()
        if not nowy_opis:
            print("Nieprawidlowe dane.")
            return
        transakcje[indeks_transakcji]["opis"] = nowy_opis
        if zapisz_transakcje(transakcje):
            print("Opis zostal zmieniony.")
        else:
            transakcje[indeks_transakcji]["opis"] = stary_opis
            print("Nie udalo sie zmienic opisu.")