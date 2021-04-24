import math
class figura():
    def __init__(self,nazwa, bok_a):
        self.nazwa = nazwa
        self.bok_a = bok_a

    def przedstaw_sie(self):
        print("Siema, to jest {}. Obliczmy moje pole i obwód.".format(self.nazwa))


class prostokat(figura):
    def __init__(self,nazwa,bok_a,bok_b):
        super().__init__(nazwa,bok_a)
        self.bok_b = bok_b
    def pole_i_obwod(self):
        print("Pole prostokąta: ",(self.bok_a * self.bok_b))
        print("Obwód prostokąta :", 2 * (self.bok_a + self.bok_b))

class kwadrat(figura):
    def __init__(self,nazwa,bok_a):
        super().__init__(nazwa,bok_a)

    def przedstaw_sie(self):
        print(f"A ja jestem kwadratem i mam wszystkie strony takie same.Policz mnie, moja strona ma {self.bok_a} cm.")

    def pole_i_obwod(self):
        print("Pole kwadrata: ",(self.bok_a * self.bok_a))
        print("Obwód kwadrata :", 4 * self.bok_a)

class trojkat(prostokat):
    def __init__(self,nazwa,bok_a,bok_b,wysokosc):
        super().__init__(nazwa,bok_a,bok_b)
        self.wysokosc = wysokosc

    def pole_i_obwod(self):
        print("Pole trójkąta: ",(1/2 * (self.bok_a*self.wysokosc)))
        print("Odwód trójkągta:",self.bok_a+self.bok_b+self.wysokosc)

class kolo(prostokat):
    def __init__(self, nazwa, bok_a, bok_b):
        super().__init__(nazwa, bok_a, bok_b)

    def pole_i_obwod(self):
            print("Pole koła: ", (self.bok_a * math.pi))
            print("Odwód koła:", (math.pi * (self.bok_b + self.bok_b)))

class romb(prostokat):
    def __init__(self, nazwa, bok_a, bok_b):
        super().__init__(nazwa, bok_a, bok_b)

    def przedstaw_sie(self):
        print(f"Z tej strony {self.nazwa}.")

    def pole_i_obwod(self):
            print("Pole rombu: ", (self.bok_a * self.bok_b))
            print("Odwód rombu:", (4 * self.bok_a))

class trapez(trojkat):
    def __init__(self,nazwa,bok_a,bok_b,bok_c,wysokosc,):
        super().__init__(nazwa,bok_a,bok_b,wysokosc)
        self.bok_c = bok_c

    def pole_i_obwod(self):
        print("Pole trapezu: ",((self.bok_a+self.bok_b)*self.wysokosc)/2)
        print("Odwód trapezu:",self.bok_a+self.bok_b+self.wysokosc+self.bok_c)
def main():
    f1 = prostokat("ptostokąt", 2,4)
    f2 = kwadrat("kwadrat", 6)
    f3 = trojkat("trójkąt", 2,5,3)
    f4 = kolo("koło",4,2)
    f5 = romb("romb",6,3)
    f6 = trapez("trapez",3,6,1,2)

    f1.przedstaw_sie()
    f1.pole_i_obwod()
    f2.przedstaw_sie()
    f2.pole_i_obwod()
    f3.pole_i_obwod()
    f4.przedstaw_sie()
    f4.pole_i_obwod()
    f5.przedstaw_sie()
    f5.pole_i_obwod()
    f6.przedstaw_sie()
    f6.pole_i_obwod()

if __name__ == "__main__":
    main()

#Siema, to jest ptostokąt. Obliczmy moje pole i obwód.
#Pole prostokąta:  8
#Obwód prostokąta : 12
#A ja jestem kwadratem i mam wszystkie strony takie same.Policz mnie, moja strona ma 6 cm.
#Pole kwadrata:  36
#Obwód kwadrata : 24
#Pole trójkąta:  3.0
#Odwód trójkągta: 10
#Siema, to jest koło. Obliczmy moje pole i obwód.
#Pole koła:  12.566370614359172
#Odwód koła: 12.566370614359172
#Z tej strony romb.
#Pole rombu:  18
#Odwód rombu: 24
#Siema, to jest trapez. Obliczmy moje pole i obwód.
#Pole trapezu:  9.0
#Odwód trapezu: 12
