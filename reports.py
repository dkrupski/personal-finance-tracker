from datetime import datetime


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


def filtruj_po_miesiacu(transakcje, rok, miesiac):

    wynik = []

    for transakcja in transakcje:
        tekst_daty = transakcja.get("data")

        if not tekst_daty:
            continue

        data = datetime.strptime(tekst_daty, "%Y-%m-%d %H:%M:%S")

        if data.year == rok and data.month == miesiac:
            wynik.append(transakcja)

    return wynik


def oblicz_raport_miesieczny(transakcje, rok, miesiac):

    transakcje_po_miesiacu = filtruj_po_miesiacu(transakcje, rok, miesiac)
    raport_miesieczny = {
        "przychody": 0,
        "wydatki": 0,
        "saldo": 0
    }

    for transakcja in transakcje_po_miesiacu:

        typ = transakcja["typ"]

        if typ == "przychod":
            raport_miesieczny["przychody"] += transakcja["kwota"]
        elif typ == "wydatek":
            raport_miesieczny["wydatki"] += transakcja["kwota"]

    raport_miesieczny["saldo"] = raport_miesieczny["przychody"] - raport_miesieczny["wydatki"]

    return raport_miesieczny


def pokaz_raport_miesieczny(transakcje):

    print("==== RAPORT MIESIECZNY ====")

    try:
        rok = int(input("Podaj rok: "))
        miesiac = int(input("Podaj miesiac: "))
    except ValueError:
        print("Podaj poprawny rok/miesiac.")
        return

    if rok <= 0:
        print("Podaj poprawny rok.")
        return
    
    if miesiac < 1 or miesiac > 12:
        print("Podaj poprawny miesiac.")
        return

    print(f"Raport za {rok}-{miesiac:02d}")

    raport = oblicz_raport_miesieczny(transakcje, rok, miesiac)

    print(f"Przychody {raport['przychody']:.2f} PLN")
    print(f"Wydatki: {raport['wydatki']:.2f} PLN")
    print(f"Saldo: {raport['saldo']:.2f} PLN")


def filtruj_po_zakresie_dat(transakcje, data_od, data_do):

    wynik = []

    for transakcja in transakcje:
        tekst_daty = transakcja.get("data")

        if not tekst_daty:
            continue

        data_transakcji = datetime.strptime(tekst_daty, "%Y-%m-%d %H:%M:%S")

        if data_od.date() <= data_transakcji.date() <= data_do.date():
            wynik.append(transakcja)

    return wynik


def pokaz_transakcje_z_zakresu(transakcje):

    print("==== TRANSAKCJE Z ZAKRESU DAT ====")

    try:
        data_od = datetime.strptime(input("Podaj date poczatkowa (RRRR-MM-DD): "), "%Y-%m-%d")
        data_do = datetime.strptime(input("Podaj date koncowa (RRRR-MM-DD): "), "%Y-%m-%d")
    except ValueError:
        print("Nieprawidlowa data")
        return

    if data_od > data_do:
        print("Data poczatkowa nie moze byc pozniejsza niz data koncowa.")
        return

    transakcje_z_zakresu = filtruj_po_zakresie_dat(transakcje, data_od, data_do)

    if not transakcje_z_zakresu:
        print("Brak transakcji w podanym zakresie.")
        return

    for numer, transakcja in enumerate(transakcje_z_zakresu, start=1):
        print(f"{numer}. [{transakcja['typ'].upper()}] {transakcja['kwota']:.2f} PLN | {transakcja['kategoria']} | {transakcja['opis']}")
        print(f"Data: {transakcja['data']}\n")


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
            data = transakcja.get("data", "Brak daty")
            print(f"{numer}. [{transakcja['typ'].upper()}] {transakcja['kwota']:.2f} PLN | {transakcja['kategoria']} | {transakcja['opis']}")
            print(f"Data: {data}\n")