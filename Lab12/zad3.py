import math
h = input("podaj długość w stopach:")
def stop (h):
    cm = float(h) * 30.48
    mm = float(h) * 3048
    km = float(h) * 0.345
    print("w cm:", cm, ',', "w mm:", mm, ",", "w km:", km)
    return cm, mm, km
print(stop(h))
