while True:
    a = int(input('podaj 1 liczbe:'))
    b = int(input('podaj 2 liczbe:'))
    c = int(input('podaj 3 liczbe:'))
    d = int(input('podaj 4 liczbe:'))
    s = ((a + b + c + d) / 4)
    if (a == 0) | (b == 0) | (c == 0) | (d == 0):
        print("podałeś liczbę  0, to jest juz koniec")
        break
    else: print(s)
