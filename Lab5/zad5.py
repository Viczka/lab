a = 0
b = 1
list = []
d = 0
while b < 100:
    c = (a + b) * ((a^2) - (a * b) + (b^2))
    a += 1
    b += 1
    print("suma sześcianów z",a ,"i",b, "równa się",c)
while True:
    d += 1
    list.append(d)
    if sum(list) >= 1000000:
        print("żeby otrzymać liczbę większą od 1000000 potrzebujemy", len(list), "liczb naturalnych" )
        break


