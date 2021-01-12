import random
a = []
for i in range (0, 10):
    a.append(random.randint(0, 15))
print("Wygenerowany ciąg:",a)
a.sort()
print(a)
y = 0
while y < len(a):
    z = a.count(a[y])
    if z>1:
        print("Liczba", a[y] ,"powtarza się", z ,"raz/y")
    y +=z
newa = list(dict.fromkeys(a))
print("Nowa tablica: ",newa)
print("Długość nowej tablicy: ",len(newa))