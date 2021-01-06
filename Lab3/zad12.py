#do zrobienia: zamienić 0 i 1 na słowa "orzel" i "reszka"
import random
list = []
while True:
    x = (random.randint(0, 1))
    list.append(x)
    if len(list) == 50:
        print(list)
        break
