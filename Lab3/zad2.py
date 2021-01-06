x = int(input("podaj :"))
while x != 0:
    x -= 1
    if (x % 6 == 0) or (x % 9 == 0):
        print(x, "podzielne przez 6 oraz 9")
    else: print(x)
