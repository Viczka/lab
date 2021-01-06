a = int(input("podaj liczbę:"))
if (a == 0):
    print("liczba równa się 0")
if(a > 0) and (a % 2 == 0):
    print("Liczba jest dodatnia i podzielna przez 2")
if(a < 0) and (a % 2 == 0):
    print("Liczba jest ujemna i podzielna przez 2")
if (a > 0) and (a % 2 != 0):
    print("liczba jest dodatnia ale nie jest podzielna przez 2")
elif (a < 0) and (a % 2 != 0):
    print("liczba jest ujemna ale nie jest podzielna przez 2")
