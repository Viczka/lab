import math
a = input("Podaj liczbe a:")
b = input("Podaj liczbe b:")
def suma (a,b):
    c = int(a) + int(b)
    return c
def różnica (a,b):
    c = int(a) - int(b)
    return c
def mnożenie (a,b):
    c = int(a) * int(b)
    return c
def dzielenie (a,b):
    c = int(a) / int(b)
    return c
def pierwiastek (a,b):
    a1 = math.sqrt(float(a))
    b1 = math.sqrt(float(b))
    return a1, b1
print("suma:", suma(a,b))
print("różnica:", różnica(a,b))
print("mnożenie:", mnożenie(a,b))
print("dzielenie:",dzielenie(a,b))
print("pierwiastek z a i b:",pierwiastek(a,b))