class Samochody():
    def __init__(self, marka, model, przebieg, kolor, rodzaj, wartosc):
        self.marka=marka
        self.model=model
        self.przebieg=przebieg
        self.kolor=kolor
        self.rodzaj=rodzaj
        self.wartosc=wartosc

    def jedzProsto(self,ile):
        self.przebieg+=ile
        return "{} {} jedzie prosto {} km".format(self.marka, self.model, ile)
    def wlaczRadio(self, muzyka):
        return "{} {} wlaczyl radio i slucha {}".format(self.marka, self.model, muzyka)
    def zmienKolor(self, innykolor):
        self.kolor=innykolor
        return "{} {} o kolorze {} zostal poddany tuningu i zmienil kolor na {}".format(self.marka, self.model, self.kolor, innykolor)
    def wystawNaRynek(self, cena):
        if self.przebieg<100000:
            cena=self.wartosc+5000
        return "{} {} zostal wystawiony na rynek za cene {}".format(self.marka, self.model, cena)
    def gruntownyTuning(self):
        self.wartosc+=150000
        return "{} {} zostal poddany tuningowi i jego wartosc zmienila sie na {}".format(self.marka, self.model, self.wartosc)
    def __str__(self):
        return f'Samochody({self.marka}, {self.model}, {self.przebieg}, {self.kolor}, {self.rodzaj}, {self.wartosc})'
samochod1=Samochody('Audi','rs7',25000,'czarny','limuzyna',750000)
samochod2=Samochody('Honda','Jazz',130000,'biel','hatchback',20000)
samochod3=Samochody('Mazda','6',30000,'czerwony','sedan',79000)
samochod4=Samochody('Porsche','911',10000,'bezowy','coupe',399000)
samochod5=Samochody('Ferrari','458',63000,'biel','kabriolet',1500000)

print(samochod1,"\n",samochod2,"\n",samochod3,"\n",samochod4,"\n",samochod5)

samochod1.jedzProsto(2500000)
k=input("Czego posluchamy? ")
samochod2.wlaczRadio(k)
l=input("Na jaki kolor przemalujemy? ")
samochod3.zmienKolor(l)
samochod4.wystawNaRynek(450000)
samochod5.gruntownyTuning()
print(samochod1,"\n",samochod2,"\n",samochod3,"\n",samochod4,"\n",samochod5)



