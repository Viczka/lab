import random
n = int(input("podaj ilość liczb:"))
i = 0
y = range(-6, 6 )
while i != n:
    i += 1
    x = int(input("Podaj liczbę:"))
    if x in y:
        print(i, ": liczba", x, "należy do przedziału (-6,6)")
    else:print(i, ": liczba", x, "nie należy do przedziału (-6,6)")









