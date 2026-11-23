import json
import os
import csv
from datetime import datetime


def zapisz_transakcje(transakcje):
    
    try: 
        with open("transakcje.tmp", "w", encoding="utf-8") as plik:
            json.dump(transakcje, plik, indent=4, ensure_ascii=False)
        os.replace("transakcje.tmp", "transakcje.json")
        return True
    except OSError as blad:
        print(f"Nie udalo sie zapisac transakcji: {blad}")
        try:
            if os.path.exists("transakcje.tmp"):
                os.remove("transakcje.tmp")
        except OSError:
            print("Nie udalo sie usunac transakcje.tmp")
        return False


def wczytaj_transakcje():

    wymagane_pola = ["typ", "kwota", "kategoria", "opis"]

    try:
        with open("transakcje.json", "r", encoding="utf-8") as plik:
            transakcje = json.load(plik)

            if not isinstance(transakcje, list):
                print("Nieprawidlowa struktura pliku JSON.")
                return None

            for transakcja in transakcje:
                if not isinstance(transakcja, dict):
                    print("Nieprawidlowa struktura transakcji.")
                    return None
                for pole in wymagane_pola:
                    if pole not in transakcja:
                        print("Nieprawidlowa struktura transakcji.")
                        return None
                if transakcja["typ"] not in ("przychod", "wydatek"):
                    print("Nieprawidlowe dane transakcji.")
                    return None
                if isinstance(transakcja["kwota"], bool) or not isinstance(transakcja["kwota"], (int, float)) or transakcja["kwota"] <= 0:
                    print("Nieprawidlowe dane transakcji.")
                    return None
                if not isinstance(transakcja["kategoria"],str) or not transakcja["kategoria"].strip():
                    print("Nieprawidlowe dane transakcji.")
                    return None
                if not isinstance(transakcja["opis"],str):
                    print("Nieprawidlowe dane transakcji.")
                    return None
                if "data" in transakcja:
                    if not isinstance(transakcja["data"], str):
                        print("Nieprawidlowa data transakcji.")
                        return None
                    try:
                        datetime.strptime(transakcja["data"], "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        print("Nieprawidlowa data transakcji.")
                        return None
                
            return transakcje
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Blad: Plik transakcje.json jest uszkodzony.")
        return None
    except OSError as blad:
        print(f"Nie udalo sie odczytac transakcji: {blad}")
        return None


def eksportuj_transakcje(transakcje):

    print("==== EKSPORT TRANSAKCJI ====")

    if not transakcje:
        print("Brak transakcji.")
        return

    with open("eksport_transakcji.csv", "w", newline="", encoding="utf-8-sig") as plik:
        writer = csv.writer(plik, delimiter=";")
        writer.writerow(["typ", "kwota", "kategoria", "opis", "data"])

        for transakcja in transakcje:
            data = transakcja.get("data", "")
            writer.writerow([transakcja["typ"], transakcja["kwota"], transakcja["kategoria"], transakcja["opis"], data])

    print("Transakcje zostaly wyeksportowane.")
