import math
r = input("podaj promień kuli:")
R = input("podaj promień podstawy stożka:")
h = input("podaj wysokość stożka:")
l = input("podaj długość tworzącej stożka:")
a = input("podaj krawędź sześcianu:")
def kula (r):
    p = 4 * math.pi * pow(int(r),2)
    v = (4 / 3) * math.pi * pow(int(r),3)
    return p, v
def stozek (R,h,l):
    p = math.pi * int(R) * (int(R) + int(l))
    v = (1 / 3) * math.pi * pow(int(R),2) * int(h)
    return p, v
def szescian (a):
    p = 6 * pow(int(a),2)
    v = pow(int(a),3)
    return p, v
print("Pole i objętość kuli:", kula(r))
print("Pole i objętość stożka:", stozek(R, h, l))
print("Pole i objętość sześcianu:", szescian(a))