import json


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


def zapisz_transakcje(transakcje):
    with open("transakcje.json", "w", encoding="utf-8") as plik:
        json.dump(transakcje, plik, indent=4, ensure_ascii=False)


def wczytaj_transakcje():

    try:
        with open("transakcje.json", "r", encoding="utf-8") as plik:
            transakcje = json.load(plik)
        return transakcje
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Blad: Plik transakcje.json jest uszkodzony.")
        return None


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
    zapisz_transakcje(transakcje)

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
    zapisz_transakcje(transakcje)

    print(f"Wydatek {kwota:.2f} PLN zostal dodany.")


def filtruj_transakcje(transakcje, typ):

    wynik = []

    if typ == "wszystkie":
        return transakcje
    
    for transakcja in transakcje:
        if transakcja["typ"] == typ:
            wynik.append(transakcja)

    return wynik


def filtruj_po_kategorii(transakcje, kategoria):

    wynik = []
 
    for transakcja in transakcje:
        if transakcja["kategoria"].strip().lower() == kategoria.strip().lower():
            wynik.append(transakcja)

    return wynik


def historia_transakcji(transakcje):

    if not transakcje:
        print("Brak transakcji.")
    else:
        print("""==== HISTORIA TRANSAKCJI ====
                
                1. Wszystkie transakcje
                2. Tylko przychody
                3. Tylko wydatki
                4. Filtruj wedlug kategorii       
        """)

        try:
            opcja = int(input("Wybierz opcje: "))
            if opcja == 1:
                wynik_filtrowania = filtruj_transakcje(transakcje, "wszystkie")
            elif opcja == 2:
                wynik_filtrowania = filtruj_transakcje(transakcje, "przychod")
            elif opcja == 3:
                wynik_filtrowania = filtruj_transakcje(transakcje, "wydatek")
            elif opcja == 4:
                kategoria = input("Podaj kategorie: ")
                wynik_filtrowania = filtruj_po_kategorii(transakcje, kategoria)
            else:
                print("Podaj opcje od 1 do 4.")
                return
        except ValueError:
            print("Podaj opcje od 1 do 4.")
            return

        if not wynik_filtrowania:
            print("Brak transakcji dla wybranego filtra.")
            return
        
        for numer, transakcja in enumerate(wynik_filtrowania, start=1):
            print(f"{numer}. [{transakcja['typ'].upper()}] {transakcja['kwota']:.2f} PLN | {transakcja['kategoria']} | {transakcja['opis']}")


def pokaz_saldo(transakcje):

    suma_przychodow = 0
    suma_wydatkow = 0

    for transakcja in transakcje:
        if transakcja["typ"] == "przychod":
            suma_przychodow += transakcja["kwota"]
        elif transakcja["typ"] == "wydatek":
            suma_wydatkow += transakcja["kwota"]

    saldo = suma_przychodow - suma_wydatkow

    print(f"Przychody: {suma_przychodow:.2f} PLN\nWydatki: {suma_wydatkow:.2f} PLN\nSaldo: {saldo:.2f} PLN")


def podsumuj_wydatki(transakcje):
   
    podsumowanie = {}

    for transakcja in transakcje:
        if transakcja["typ"] == "wydatek":
            kategoria = transakcja["kategoria"].strip().lower()
            
            if kategoria in podsumowanie:
                podsumowanie[kategoria] += transakcja["kwota"]
            else:
                podsumowanie[kategoria] = transakcja["kwota"]

    return podsumowanie


def pokaz_podsumowanie_wydatkow(transakcje):

    print("==== WYDATKI WEDLUG KATEGORII ====\n")

    podsumowanie = podsumuj_wydatki(transakcje)

    if not podsumowanie:
        print("Brak wydatkow")
        return

    for kategoria, suma in podsumowanie.items():
        print(f"{kategoria}: {suma:.2f} PLN")

    laczne_wydatki = sum(podsumowanie.values())

    print(f"\nLaczne wydatki: {laczne_wydatki:.2f} PLN")


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
        6. Zakoncz
        """)

        try:
            opcja = int(input("Wybierz opcje: "))
        except ValueError:
            print("Podaj opcje od 1 do 6.")
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
            is_run = False
        else:
            print("Podaj opcje od 1 do 6.")


def main():

    transakcje = wczytaj_transakcje()

    if transakcje is None:
        return
    
    pokaz_menu(transakcje)


if __name__ == "__main__":
    main()
