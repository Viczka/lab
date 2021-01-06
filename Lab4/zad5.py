liczby = []
while True:
    x = int(input("podaj liczbę:"))
    if x == 0:
        print("Podaj poprawna liczbę")
    liczby.append(x)
    if sum(liczby) > 100:
        print("suma przekracza 100")
        break
    else:continue
y = (sum(liczby) / len(liczby))
if y >= 66:
    print("srednia wynosi",y, ",to za dużo")
