import math
def netto (brutto):
    print("Ubezpieczenie emerytalne -","{:.3f}".format(float(brutto) * 0.0976), "pln")
    print("Ubezpieczenie rentowe -","{:.3f}".format(float(brutto) * 0.015), "pln")
    print("Ubezpieczenie chorobowe -","{:.3f}".format(float(brutto) * 0.0245), "pln")
    print("Ubezpieczenie zdrowotne -","{:.3f}".format(float(brutto) * 0.0777), "pln")
    print("Zaliczka na PIT -","{:.3f}".format(float(brutto) * 0.0489), "pln")
    print("Kwota netto -", "{:.3f}".format(float(brutto) * 0.7363), "pln")
    print("Kwota brutto -","{:.3f}".format(float(brutto)), "pln")
def menu():
    brutto = float(input("Podaj wynagrodzenie brutto:"))
    print(netto(brutto))
menu()