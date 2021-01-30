h = float(input("Na jakiej wysokości lecimy?[w metrach]:"))
def wysokosc (h):
    a = float(h) / 1000
    if a > 5:
        print("Na tej wysokości jesteś już bezpieczny.")
    else: print(a, 'km to za nisko!')
wysokosc(h)



