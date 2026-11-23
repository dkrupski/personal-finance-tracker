import json
import os

from storage import zapisz_transakcje, wczytaj_transakcje


def test_zapisz_transakcje(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    transakcje = [
        {
            "typ": "przychod",
            "kwota": 2500,
            "kategoria": "Pensja",
            "opis": "Wynagrodzenie",
            "data": "2026-11-20 10:00:00"
        }
    ]

    wynik = zapisz_transakcje(transakcje)

    assert wynik is True
    assert os.path.exists("transakcje.json")

    with open("transakcje.json", "r", encoding="utf-8") as plik:
        zapisane_dane = json.load(plik)

    assert zapisane_dane == transakcje
    assert not os.path.exists("transakcje.tmp")


def test_wczytaj_transakcje(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    transakcje = [
        {
            "typ": "wydatek",
            "kwota": 150,
            "kategoria": "Jedzenie",
            "opis": "Zakupy",
            "data": "2026-11-20 12:00:00"
        }
    ]

    zapisz_transakcje(transakcje)

    wynik = wczytaj_transakcje()

    assert wynik == transakcje
    assert wynik[0]["kwota"] == 150


def test_wczytaj_uszkodzony_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    with open("transakcje.json", "w", encoding="utf-8") as plik:
        plik.write('{"typ": "przychod", "kwota": 1000')

    wynik = wczytaj_transakcje()

    assert wynik is None