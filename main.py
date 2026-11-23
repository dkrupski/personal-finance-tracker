from storage import (wczytaj_transakcje, 
                     eksportuj_transakcje)
from transactions import (dodaj_przychod,
                           dodaj_wydatek,
                           edytuj_transakcje,
                           usun_transakcje)
from reports import (pokaz_saldo, 
                     pokaz_podsumowanie_wydatkow,
                     pokaz_raport_miesieczny,
                     pokaz_transakcje_z_zakresu,
                     historia_transakcji)


def pokaz_menu(transakcje):

    is_run = True

    while is_run:

        print("""
        ==== PERSONAL FINANCE TRACKER ====

        1. Dodaj przychod
        2. Dodaj wydatek
        3. Historia transakcji
        4. Pokaz saldo
        5. Podsumowanie wydatkow
        6. Raport miesieczny
        7. Filtruj transakcje wedlug dat
        8. Usun transakcje
        9. Edytuj transakcje
        10. Eksportuj transakcje do CSV
        11. Zakoncz
        """)

        try:
            opcja = int(input("Wybierz opcje: "))
        except ValueError:
            print("Podaj opcje od 1 do 11.")
            continue

        if opcja == 1:
            dodaj_przychod(transakcje)
        elif opcja == 2:
            dodaj_wydatek(transakcje)
        elif opcja == 3:
            historia_transakcji(transakcje)
        elif opcja == 4:
            pokaz_saldo(transakcje)
        elif opcja == 5:
            pokaz_podsumowanie_wydatkow(transakcje)
        elif opcja == 6:
            pokaz_raport_miesieczny(transakcje)
        elif opcja == 7:
            pokaz_transakcje_z_zakresu(transakcje)
        elif opcja == 8:
            usun_transakcje(transakcje)
        elif opcja == 9:
            edytuj_transakcje(transakcje)
        elif opcja == 10:
            eksportuj_transakcje(transakcje)
        elif opcja == 11:
            is_run = False
        else:
            print("Podaj opcje od 1 do 11.")


def main():

    transakcje = wczytaj_transakcje()

    if transakcje is None:
        return
    
    pokaz_menu(transakcje)


if __name__ == "__main__":
    main()
