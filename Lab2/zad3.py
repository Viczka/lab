a = int(input("podaj liczbę a:"))
b = int(input("podaj liczbę b:"))
c = int(input("podaj liczbę c:"))
if (a > b) and (a > c):
    print("liczba a jest największa")
if (b > a) and (b > c):
    print("liczba b jest największa")
if (c > a) and (c > a):
    print("liczba c jest największa")
elif (a == b) or (a == c):
    print("liczby są identyczne")
