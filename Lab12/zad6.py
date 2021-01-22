x = int(input("Podaj liczbę całkowitą:"))
def binar (x):
    return bin(x)[2:]
def heks (x):
    return hex(x)[2:]
def okt (x):
    return oct(x)[2:]
def heks2 (x):
    a = bin(x)[2:]
    return hex(int(a))[2:]
print("postać binarna:",binar(x))
print("postać szesnastkowa:", heks(x))
print("postaća ósemkowa:",okt(x))
print("postać szesnastkowa z binarnej:",heks2(x))

