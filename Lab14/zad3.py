import math
class figura():
    def __init__(self,nazwa, a):
        self.nazwa = nazwa
        self.a = a

    def przedstaw_sie(self):
        print("Siema, to jest {}. Obliczmy moje pole i obwód.".format(self.nazwa))

class prostokat(figura):
    def __init__(self,nazwa,a,b):
        super().__init__(nazwa,a)
        self.b = b
    def pole_i_obwod(self):
        print("Pole prostokąta: ",(self.a * self.b))
        print("Obwód prostokąta :", 2 * (self.a + self.b))

class kwadrat(figura):
    def __init__(self,nazwa,a):
        super().__init__(nazwa,a)

    def przedstaw_sie(self):
        print(f"Jestem kwadratem i mam wszystkie strony takie same.Policz mnie, moja strona ma {self.a} cm.")

    def pole_i_obwod(self):
        print("Pole kwadrata: ",(self.a * self.a))
        print("Obwód kwadrata :", 4 * self.a)

class trojkat(prostokat):
    def __init__(self,nazwa,a,b,c,h):
        super().__init__(nazwa,a,b)
        self.c = c
        self.h = h

    def pole_i_obwod(self):
        print("Pole trójkąta: ",(1/2 * (self.a*self.h)))
        print("Odwód trójkągta:",self.a+self.b+self.c)

class kolo(figura):
    def __init__(self, nazwa, a):
        super().__init__(nazwa, a)

    def pole_i_obwod(self):
            print("Pole koła: ", (math.pi * (self.a ** 2) ))
            print("Odwód koła:", (2 * math.pi * self.a))

class romb(trojkat):
    def __init__(self, nazwa, a, h):
        super().__init__(nazwa, a,h)

    def przedstaw_sie(self):
        print(f"Z tej strony {self.nazwa}.")

    def pole_i_obwod(self):
        print("Pole rombu: ", (self.a * self.h))
        print("Odwód rombu:", (4 * self.a))

class trapez(trojkat):
    def __init__(self, nazwa, a,b,c,d,h):
        super().__init__(nazwa, a,b,c,h)
        self.d=d

    def pole_i_obwod(self):
        print("Pole trapezu: ", (1/2 * (self.a+self.b) * self.h))
        print("Odwód trapezu:", self.a + self.b + self.c + self.d)

    f = {
    1 : 'Prostokat',
    2 : 'Kwadrat',
    3 : 'Trójkat',
    4 : 'Koło',
    5 : 'Romb',
    6 : 'Trapez'}

    print(f)
    k = float(input("Podaj numer figury, którą chcesz obliczyć : "))
    if k == 0 or k > 6 or k < 0:
        print("Niema takiego numeru.")
    if k == 1:
        f1 = prostokat("prostokąt",a=float(input("Podaj strone a : ")),b=float(input("Podaj strone b : ")))
        f1.przedstaw_sie()
        f1.pole_i_obwod()
    if k == 2:
        f2 = kwadrat("kwadrat", a=float(input("Podaj strone a : ")))
        f2.przedstaw_sie()
        f2.pole_i_obwod()
    if k == 3:
        f3 = trojkat("trójkąt",a=float(input("Podaj strone a : ")),b=float(input("Podaj strone b : ")),c=float(input("Podaj strone c : ")),h=float(input("Podaj wysokość : ")))
        f3.pole_i_obwod()
    if k == 4:
        f4 = kolo("koło", a=float(input("Podaj promień : ")))
        f4.pole_i_obwod()
    if k == 5:
        f5 = romb("romb",a=float(input("Podaj strone a : ")),h=float(input("Podaj wysokość : ")))
        f5.przedstaw_sie()
        f5.pole_i_obwod()
    if k == 6:
        f6 = trapez("trapez",a=float(input("Podaj strone a : ")),b=float(input("Podaj strone b : ")),c=float(input("Podaj strone c : ")),d=float(input("Podaj strone d : ")),h=float(input("Podaj wysokość : ")))
        f6.pole_i_obwod()
