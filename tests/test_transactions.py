from transactions import dodaj_przychod


def test_dodaj_przychod(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    odpowiedzi = iter([
        "2500",
        "Pensja",
        "Wynagrodzenie"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(odpowiedzi)
    )

    transakcje = []

    dodaj_przychod(transakcje)

    assert len(transakcje) == 1
    assert transakcje[0]["typ"] == "przychod"
    assert transakcje[0]["kwota"] == 2500
