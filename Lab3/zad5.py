# I metoda
n = int(input("Podaj liczbę do obliczenia silni: "))
i = 1
for a in range(1, n+1):
    i = i * a
print("Silnia z liczby ", n, "to ", i)



# II metoda
import math
n = int(input("podaj liczbę:"))
print("silnia", math.factorial(n))
