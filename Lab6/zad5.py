# do poprawki ilość wystąpień el. w liście
import random
a = []
b = []
x = int(input("Podaj ile liczb ma posiadać ciąg a:"))
start = int(input("Podaj początkową wartość ciągu:"))
stop = int(input("Podaj końcową wartość ciągu:"))
while len(a) != x:
        a.append(random.randrange(start, stop))
        if len(a) == x:
            print("To jest ciąg wygenerowany a:",a)
            print("Trzeci el. od końca to:",a[-3])
y = int(input("Podaj który el. od końca chcesz usunąć:"))
a.pop(-y)
print("Usuneliśmy",y,"element od końca:",a)
# II ciąg
x = int(input("Podaj ile liczb ma posiadać ciąg b:"))
start = int(input("Podaj początkową wartość ciągu:"))
stop = int(input("Podaj końcową wartość ciągu:"))
while len(b) != x:
        b.append(random.randrange(start, stop))
        if len(b) == x:
            print("To jest ciąg wygenerowany b:",b)
c = a + b
print("Połączyliśmy ciągi a i b:",c)
print("Długość ciągu c:",len(c))
i = 0
while True:
    if c.count(c[i]) >= 2:
        print("Liczba", c[i], "powtarza się i występuje", c.count(c[i]),"razy")
    else:print("Liczba", c[i], "występuje 1 raz")
    i += 1
    if i == len(c):
        break