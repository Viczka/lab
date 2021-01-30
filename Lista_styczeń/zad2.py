def koszt_pracodawcy(brutto):
    print("Pracodawda wydaje:")
    print("Ubezpieczenie emerytalne -","{:.3f}".format(float(brutto) * 0.0976), "pln")
    print("Ubezpieczenie rentowe -","{:.3f}".format(float(brutto) * 0.065), "pln")
    print("Wypadkowe -","{:.3f}".format(float(brutto) * 0.0167), "pln")
    print("Fundusz pracy -","{:.3f}".format(float(brutto) * 0.0245), "pln")
    print("FGŚP -","{:.3f}".format(float(brutto) * 0.01),"pln")
    print("Kwota brutto -", "{:.3f}".format(float(brutto)), "pln")
    return
def menu():
    brutto = float(input("Podaj wynagrodzenie brutto:"))
    print(koszt_pracodawcy(brutto))
menu()

