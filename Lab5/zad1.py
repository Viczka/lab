import random
list = []
list1 = []
x = int(input("podaj ilość liczb:"))
for i in range(x):
    y = random.randrange(-100, 100)
    list.append(y)
    if y > 0 :
        list1.append(y)
    if len(list) == x:
        print("caly ciąg:", list)
        print("ciąg liczb dodatnich:", list1)
for a in list1:
    sr = sum(list1)/len(list1)
    print("srednia liczb dodatnich:", sr)
    break
