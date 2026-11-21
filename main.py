def dodaj_przychod(transakcje):


    while True:
        try:
            kwota = float(input("Podaj kwote: "))
            if kwota <= 0:
                print("Kwota musi byc wieksza od zera.")
                continue
            break
        except ValueError:
            print("Nieprawidlowa kwota.")
            continue

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


def dodaj_wydatek():
    pass


def historia_transakcji():
    pass


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
            print("Dodaj wydatek")
        elif opcja == 3:
            print("Historia teanskacji")
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