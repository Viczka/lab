import random
a = []
for i in range(10):
    a.append(random.randint(0, 100))
    if i == 9:
        print("Wygenerowana lista:",a)
min = 1
max = 0
random.shuffle(a)
print("Mieszna lista:",a)
a.sort()
print("Posortowana rosnąco:", a)
a.sort(reverse=True)
print("Posortowana malejąco:", a)