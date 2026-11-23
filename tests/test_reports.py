from reports import podsumuj_wydatki, oblicz_raport_miesieczny, filtruj_transakcje, filtruj_po_kategorii, filtruj_po_zakresie_dat
from datetime import datetime


def test_podsumuj_wydatki():
    transakcje = [
        {"typ": "wydatek", "kwota": 50, "kategoria": "Jedzenie"},
        {"typ": "wydatek", "kwota": 30, "kategoria": "Transport"},
        {"typ": "wydatek", "kwota": 25, "kategoria": "Jedzenie"},
        {"typ": "przychod", "kwota": 1000, "kategoria": "Pensja"},
    ]

    wynik = podsumuj_wydatki(transakcje)

    assert wynik["jedzenie"] == 75
    assert wynik["transport"] == 30
    assert "pensja" not in wynik


def test_podsumuj_wydatki_pusta_lista():
    transakcje = []

    wynik = podsumuj_wydatki(transakcje)

    assert wynik == {}


def test_podsumuj_wydatki_rozne_zapisy_kategorii():
    transakcje = [
        {"typ": "wydatek", "kwota": 20, "kategoria": "Jedzenie"},
        {"typ": "wydatek", "kwota": 30, "kategoria": "JEDZENIE"},
        {"typ": "wydatek", "kwota": 15, "kategoria": " jedzenie "},
    ]

    wynik = podsumuj_wydatki(transakcje)

    assert wynik["jedzenie"] == 65
    assert len(wynik) == 1


def test_oblicz_raport_miesieczny():
    transakcje = [
        {"typ": "przychod", "kwota": 3000, "data": "2026-11-05 10:00:00"},
        {"typ": "wydatek", "kwota": 500, "data": "2026-11-10 12:00:00"},
        {"typ": "wydatek", "kwota": 200, "data": "2026-11-15 15:00:00"},
        {"typ": "przychod", "kwota": 1000, "data": "2026-10-20 09:00:00"},
    ]

    wynik = oblicz_raport_miesieczny(transakcje, 2026, 11)

    assert wynik["przychody"] == 3000
    assert wynik["wydatki"] == 700
    assert wynik["saldo"] == 2300


def test_raport_miesieczny_bez_transakcji():
    transakcje = [
        {"typ": "przychod", "kwota": 2000, "data": "2026-11-10 10:00:00"},
        {"typ": "wydatek", "kwota": 300, "data": "2026-11-15 12:00:00"},
    ]

    wynik = oblicz_raport_miesieczny(transakcje, 2026, 12)

    assert wynik == {"przychody": 0, "wydatki": 0, "saldo": 0}


def test_filtruj_transakcje_przychody():
    transakcje = [
        {"typ": "przychod", "kwota": 3000},
        {"typ": "wydatek", "kwota": 500},
        {"typ": "przychod", "kwota": 1000},
    ]

    wynik = filtruj_transakcje(transakcje, "przychod")

    assert len(wynik) == 2
    assert wynik[0]["kwota"] == 3000


def test_filtruj_po_kategorii():
    transakcje = [
        {"typ": "wydatek", "kwota": 50, "kategoria": "Jedzenie"},
        {"typ": "wydatek", "kwota": 30, "kategoria": "Transport"},
        {"typ": "wydatek", "kwota": 25, "kategoria": " JEDZENIE "},
    ]

    wynik = filtruj_po_kategorii(transakcje, "jedzenie")

    assert len(wynik) == 2
    assert wynik[0]["kwota"] == 50
    assert wynik[1]["kwota"] == 25


def test_filtruj_po_zakresie_dat():
    transakcje = [
        {"typ": "przychod", "kwota": 3000, "data": "2026-11-05 10:00:00"},
        {"typ": "wydatek", "kwota": 100, "data": "2026-11-15 12:00:00"},
        {"typ": "wydatek", "kwota": 200, "data": "2026-12-01 09:00:00"},
    ]

    data_od = datetime(2026, 11, 1)
    data_do = datetime(2026, 11, 30)

    wynik = filtruj_po_zakresie_dat(transakcje, data_od, data_do)

    assert len(wynik) == 2
    assert wynik[0]["kwota"] == 3000
    assert wynik[1]["kwota"] == 100


