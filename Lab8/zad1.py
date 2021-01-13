menu = {
"Amerykańska" : 20.00,
"Wegeteriańska" : 26.50,
"Hawajska" : 19.50,
"Paperoni" : 21.00,
"Serowa" : 24.00,
"Salami" : 18.50,
"Mięsna" : 28.00,
"Wiosenna" : 23.00,
"Capriciosa" : 23.50,
"Margherita" : 16.00
}
print("Menu:",menu)
y = 1
x = 1
for cena in menu.values():
    print("Cena", x, "pizzy:", cena)
    x += 1
for name in menu.keys():
    print(y ,"pizza:", name)
    y += 1
for pizza in menu.items():
    print(pizza)
max_c = max(menu.values())
min_c = min(menu.values())
max_k = max(keys for keys, values in menu.items() if values == max_c)
min_k = min(keys for keys, values in menu.items() if values == min_c)
del menu[max_k]
del menu[min_k]
print(menu)
name = input("Podaj nazwe: ")
cena = float(input("Podaj cene: "))
menu[name] = cena
print(menu)