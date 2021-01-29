from zad1 import netto

def koszt_pracodawcy(brutto):
    emerytalne = brutto * 0.0976
    rentowa = brutto * 0.065
    wypadkowa = brutto * 0.0167
    fundusz = brutto * 0.0245
    fgsp = brutto * 0.01
    return brutto + emerytalne + rentowa + wypadkowa + fundusz + fgsp


if __name__ == "__main__":
    brutto = float(input("Podaj kwotę brutto: "))
    print(f"Należy Ci się: {koszt_pracodawcy(brutto)} zł")
    print(f"Dostajesz na rękę: {netto(brutto)} zł")