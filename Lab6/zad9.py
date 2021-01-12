x = int(input("Ile liczb powinienen zawierać ciąg:"))
a = []
for i in range(x):
    a.append(int(input("Podaj liczbę:")))
    if len(a) == x:
        print(a)
print("Maksymalna liczba:",max(a),". Występuje",a.count(max(a)),"raz/y")