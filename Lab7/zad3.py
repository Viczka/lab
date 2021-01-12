import random
a = ()
b = ()
while len(a) < 100:
    for i in range(0,100):
        a = a + (random.randrange(0, 101, 2),)
while len(b) < 100:
    for i in range(0,100):
        b = b + (random.randrange(1, 101, 2),)
        break
print("Krotka parzysta:", a)
print("Krotka nieparzysta:",b)
c = a[0:100] + b[0:100]
print("Konkatenacja:", c)
print("Długość:", len(c))
if 0 in c:
    print("Krotka zawiera element zero")
if 100 in c:
    print("Krotka zawiera element 100")
print("Miejsce w pamięci:", id(c))

