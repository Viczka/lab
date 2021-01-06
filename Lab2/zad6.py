a = int(input("podaj liczbe 1:"))
b = int(input("podaj liczbe 2:"))
c = int(input("podaj liczbe 3:"))
d = int(input("podaj liczbe 4:"))
m = a
if (a > b) and (a > c) and (a > d):
    print("Liczba", a ,"jest największa")
if (b > a) and (b > c) and (b > d):
    print("Liczba", b, "jest największa")
if (c > b) and (c > a) and (c > d):
    print("Liczba", c ,"jest największa")
elif (d > b) and (d > c) and (d > a):
    print("Liczba", d ,"jest największa")
