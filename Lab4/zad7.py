while True:
    x = int(input("Podaj liczbę:"))
    if (x == 1) or (x == 0):
        print(x, "nie jest licbą pierwsza")
        break
    if (x == 2) or (x == 3):
        print(x, "jest liczbą pierwszą")
    elif (x % 1 == 0) and (x % x == 0) and ((x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0) or (x % 7 == 0)):
        print(x,"nie jest liczbą pierwszą")
    else:print(x,"jest liczbą pierwszą")
