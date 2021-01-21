# do poprawy - zrobić żeby zwracał dane typu float
h = float(input("Na jakiej wysokości lecimy?[w metrach]:"))
def wysokosc (h):
    a = float(h) / 1000
    if a < 5:
        return a
    else:return "Na tej wysokości jesteś już bezpieczny"
print(wysokosc(h),'km to za nisko!')
