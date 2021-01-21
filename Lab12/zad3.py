import math
h = float(input("podaj długość w stopach:"))
def cm (h):
    cm = float(h) * 30.48
    return cm
def mm (h):
    mm = float(h) * 3048
    return mm
def km (h):
    km = float(h) * 0.0003048
    return km
print(cm(h),'cm')
print(mm(h),'mm')
print(km(h),'km')

