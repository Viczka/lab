x = int(input("Podaj liczbę:"))
if x == 0:
    print("Podałeś liczbę zero")
a = 0
list = []
while a != x:
    a += 1
    if x % a == 0:
        list.append(a)
    if a == x:
        print("Dzielniki liczby",x,"to:",list)





