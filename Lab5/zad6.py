import random
n = random.randint(1, 100)
x = 0
i = 0
print("Zgadnij liczbę z zakresu 1-100!")
while x != n and i < 3:
    x = int(input("Podaj liczbę: "))
    if x == n:
        print("Gratulacje Wygrałeś! Twoją liczbą była: ", n)
    else:
        if x > n:
            print("Podałeś za dużą wartość")
            i += 1
        if n > x:
            print("Podałeś za małą wartość")
            i += 1
        if i == 3:
            print("Przegrałeś, prawidłowa odpowiedź: ", n)


