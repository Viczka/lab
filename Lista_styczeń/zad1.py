# zrobiłam 1 i 2 zadania za pomocą Google. Nie do końca jeszcze rozumiem jak działają, ale spróbuję ogarnąć
def netto(kwota_brutto):
    emerytalna = 0.0976 * kwota_brutto
    rentowa = 0.015 * kwota_brutto
    chorobowa = 0.0245 * kwota_brutto
    podstawa = kwota_brutto - (emerytalna + rentowa + chorobowa)
    zdrowotna = podstawa * 0.09
    p = emerytalna + rentowa + chorobowa + zdrowotna
    kwota = kwota_brutto - p
    zus_odliczenie = podstawa * 0.0775
    zaliczka = kwota * 0.17 - 43.76 - zus_odliczenie
    if zaliczka < 0:
        zaliczka = 0

    return round(kwota_brutto - (emerytalna + rentowa + chorobowa + zdrowotna + zaliczka), 2)


if __name__ == "__main__":

    kwota = float(input("Podaj kwote brutto: "))
    print(f"Kwota netto: {netto(kwota)} zł")
    zabiera = kwota - netto(kwota)
    print(f"Dla Państwa:  {zabiera} zł ")