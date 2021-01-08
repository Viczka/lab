import random
tab = []
i = 0
while i < 10:
    a = int(input("Podaj liczbę: "))
    if a > 60 or a < -1:
        print("Podaj liczbę z zakresu 1 - 60:")
        continue
    else:
        tab.append(a)
        i += 1
print(tab)
print("Teraz wykorzystamy metodę 'insert'")
insert = 0
while insert < 3:
    index = int(input("Podaj index el. w tab:"))
    liczba = random.randrange(0, 60, 2)
    tab.insert(index, liczba)
    insert  += 1
print("Dodaliśmy dowolne elementy za pomocą 'insert':",tab)
print("Teraz wykorzystamy metodę 'append'")
append = 0
while append < 4:
    liczba = random.randrange(0, 60, 2)
    tab.append(liczba)
    append += 1
print("Dodaliśmy dowolne elementy za pomocą 'append':",tab)
print("Teraz wykorzystamy metodę 'remove'")
remove = 0
while remove < 3:
    x = int(input("Podaj element nieparzysty z tablicy:"))
    if x % 2 == 0:
        print("Podałeś liczbę parzystą")
        continue
    else:
        tab.remove(x)
        remove += 1
print("Usuneliśmy elementy za pomocą 'remove':",tab)
print("Teraz wykorzystamy metodę 'pop'")
pop = 0
while pop < 3:
    index = int(input("Podaj index el. z tab:"))
    pop += 1
    tab.pop(index)
print("Usuneliśmy elementy za pomocą 'pop':",tab)
print("Teraz zamienimy el. 5 i 10 na 3 i 33")
tab[5] = 3
tab[10] = 33
print(tab)