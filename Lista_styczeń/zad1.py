import math
def netto(x):
    z = float(x) * 100 / 73.63
    print("Ubezpieczenie emerytalne -","{:.3f}".format(float(z) * 9.76 / 100), "pln")
    print("Ubezpieczenie rentowe -","{:.3f}".format(float(z) * 1.5 / 100), "pln")
    print("Ubezpieczenie chorobowe -","{:.3f}".format(float(z) * 2.45 / 100), "pln")
    print("Ubezpieczenie zdrowotne -","{:.3f}".format(float(z) * 7.77 / 100), "pln")
    print("Zaliczka na PIT -","{:.3f}".format(float(z) * 4.89 / 100), "pln")
    print("Kwota brutto -","{:.3f}".format(float(z)), "pln")
def brutto(y):
    print("Ubezpieczenie emerytalne -","{:.3f}".format(float(y) * 9.76 /100), "pln")
    print("Ubezpieczenie rentowe -","{:.3f}".format(float(y) * 1.5 / 100), "pln")
    print("Ubezpieczenie chorobowe -","{:.3f}".format(float(y) * 2.45 / 100), "pln")
    print("Ubezpieczenie zdrowotne -","{:.3f}".format(float(y) * 7.77 / 100), "pln")
    print("Zaliczka na PIT -","{:.3f}".format(float(y) * 4.89 / 100), "pln")
    print("Kwota netto -","{:.3f}".format(float(y) * 73.63 / 100), "pln")
def menu():
    options = ['1 - netto',
               '2 - brutto']
    for i in range(0,len(options)):
        print(options[i])
    a = int(input("Podaj numer opcji, którą chcesz obliczyć:"))
    if a == 1:
        x = input("Podaj wynagrodzenie netto:")
        print(netto(x))
    if a == 2:
        y = input("Podaj wynagrodzenie brutto:")
        print(brutto(y))
    elif a != 1 and a != 2:
        print("Niema takiej opcji.")
menu()
