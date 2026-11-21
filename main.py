def dodaj_przychod():
    pass


def dodaj_wydatek():
    pass


def historia_transakcji():
    pass


def pokaz_saldo():
    pass


def pokaz_menu():

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
            print("Dodaj przychod")
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
    pokaz_menu()


if __name__ == "__main__":
    main()