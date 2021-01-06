suma = 0
list = []
i = 0
while True:
    a = int(input("Podaj liczbę a:"))
    list.append(a)
    print(list)
    suma = suma + list[i]
    i += 1
    if len(list) >= 2:
        if a == list[-2]:
            print("Podałeś taką samą liczbę")
            break
        else:print("suma wynosi",suma)
