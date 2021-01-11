x = int(input("Podaj liczbę:"))
a = 0
list = []
while True:
    if a == 0:
        a += 1
    if x % a == 0:
        list.append(a)
        a += 1
        print(list)
    continue
