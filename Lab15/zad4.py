import random
class Karta:
    def __init__(self, numer,figura):
        self.numer = numer
        self.figura = figura

    def __repr__(self):
        return "{} {}".format(self.numer, self.figura)

class Talia(Karta):
    numer = ["As","2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król"]
    figura = ["Wino", "Kier", "Trefl","Karo"]
    talia1 = []

    def __init__(self,numer,figura):
        super().__init__(numer,figura)

    def __add__(self, other):
        return Talia(self.numer+other.numer, self.figura+other.figura)

    def tw_talii(self):
        for i in self.numer:
            self.talia1.append(Karta(i, self.figura[0]))
        for i in self.numer:
            self.talia1.append(Karta(i, self.figura[1]))
        for i in self.numer:
            self.talia1.append(Karta(i, self.figura[2]))
        for i in self.numer:
            self.talia1.append(Karta(i, self.figura[3]))

    def sort_numer(self):
        print(sorted(self.talia1, key=lambda Karta: Karta.numer))

    def sort_figura(self):
        print(sorted(self.talia1, key=lambda Karta: Karta.figura))

    def shuffle(self):
        random.shuffle(self.talia1)

    def pokaz_karte(self, numer, figura):
        for i in self.talia1:
            if i.numer == numer and i.figura == figura:
                print("{} {} jest w talii".format(i.numer, i.figura))
                if i.numer != numer and i.figura != figura:
                    print("Niema takiej karty")

    def usun(self):
        x = int(input("Podaj numer karty którą chcesz usunąć (1-52): "))
        del p.talia1[x]

p = Talia(Talia.numer,Talia.figura)
p.tw_talii()
p.shuffle()
print("Twój zestaw do gry: ",Talia.talia1)
print(p.pokaz_karte('6','Wino'))
p1 = Talia(Talia.numer,Talia.figura)
p2 = Talia(Talia.figura,Talia.numer)
p3 = p1 + p2
print(p3.numer)
print(p3.figura)
print(p.usun())
print(Talia.talia1)