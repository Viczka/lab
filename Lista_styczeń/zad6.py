def fahrenheit (number):
    C = (number - 32) * 5/9
    print(number,"°F =", round(C, 2),"°C")
    if (C <= 0):
        print("Woda zamarza, przy 0 stopniach Celcjusza")
    elif (C >= 100):
        print("Woda wrze przy 100 stopniach Celcjusza, możesz robić herbatkę!")
    K = (number - 32) / 1.8000 + 273.15
    print(number, "°F =", round(K, 2), "K")
def cilsjusz (number):
    F = number * 9/5 + 32
    if (F <= 32):
        print("Woda zamarza przy 32 stopniach Fahrenheita!")
    elif (F >= 212) :
              print("Woda wrze przy 212 stopniach Fahrenheita!")
    print(number, "°C =", round(F, 2), "°F")
    K = number + 273.15
    print(number, "°C =", round(K, 2), "K")
def kelwin (number):
    C = number + -273.15
    print(number, "K =", round(C, 2), "°C")
    F = (number - 273.15) * 1.8 + 32.00
    print(number, "K =", round(F, 2), "℉")
    if (F <= 32):
        print("Woda zamarza przy 32 stopniach Fahrenheita!")
    elif (F >= 212):
        print("Woda wrze przy 212 stopniach Fahrenheita!")
        if (C <= 0):
            print("Woda zamarza, przy 0 stopniach Celcjusza")
        elif (C >= 100):
            print("Woda wrze przy 100 stopniach Celcjusza!")
def menu():
    wybor = input("Wpisz jakie stopnie chcesz przeliczyć [K,C,F]:").upper()
    number = float(input("Wpisz liczbę stopni: "))
    if wybor == 'F':
        print(fahrenheit(number))
    if wybor == 'C':
        print(cilsjusz(number))
    if wybor == 'K':
        print(kelwin(number))
menu()
