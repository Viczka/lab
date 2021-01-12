import random
tup = ()
p = []
np = []
for x in range(0, 100):
    tup = tup + (random.randint(0, 10),)
    if len(tup) == 99:
        print(tup)
        if 0 in tup:
            print("Ilość wystąpień '0 - zero':",tup.count(0))
            if 1 in tup:
                print("Ilość wystąpień '1 - jedunki':", tup.count(1))
        print("Ilość wystąpień '2 - dwójki':", tup.count(2))
i = 0
for i in range(0,100):
    if tup[i] % 2 == 0:
        p.append(tup[i])
    else:np.append(tup[i])
    i += 1
    if i == len(tup):
        print("Parzyste elementy:", p)
        print("Nieparzyste elementy:", np)
