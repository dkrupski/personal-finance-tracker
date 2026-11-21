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
        "opis": opis
    }

    transakcje.append(slownik_transakcji)

    print(f"Przychod {kwota:.2f} PLN zostal dodany.")


def dodaj_wydatek(transakcje):

    kwota = pobierz_kwote()
    kategoria = input("Podaj kategorie: ")
    opis = input("Podaj opis: ")

    slownik_transakcji = {
        "typ": "wydatek",
        "kwota": kwota,
        "kategoria": kategoria,
        "opis": opis
    }

    transakcje.append(slownik_transakcji)

    print(f"Wydatek {kwota:.2f} PLN zostal dodany.")


def historia_transakcji(transakcje):
    
    print("==== HISTORIA TRANSAKCJI ====")

    if not transakcje:
        print("Brak transakcji.")
    else:
        for numer, transakcja in enumerate(transakcje, start=1):
            print(f"{numer}. [{transakcja['typ'].upper()}] {transakcja['kwota']:.2f} PLN | {transakcja['kategoria']} | {transakcja['opis']}")


def pokaz_saldo():
    pass


def pokaz_menu(transakcje):

    is_run = True

    while is_run:

        print("""
        ==== PERSONAL FINANCE TRACKER ====

        1. Dodaj przychod
        2. Dodaj wydatek
        3. Historia transakcji
        4. Pokaz saldo
        5. Zakoncz
        """)

        try:
            opcja = int(input("Wybierz opcje: "))
        except ValueError:
            print("Podaj opcje od 1 do 5.")
            continue

        if opcja == 1:
            dodaj_przychod(transakcje)
        elif opcja == 2:
            dodaj_wydatek(transakcje)
        elif opcja == 3:
            historia_transakcji(transakcje)
        elif opcja == 4:
            print("Pokaz saldo")
        elif opcja == 5:
            is_run = False
        else:
            print("Nieprawidlowa opcja")


def main():
    transakcje = []
    pokaz_menu(transakcje)


if __name__ == "__main__":
    main()