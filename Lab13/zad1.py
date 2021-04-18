class car():
    species = "smochód"
    def __init__(self, marka, model, typ, przebieg, kolor, cena):
        self.marka = marka
        self.model = model
        self.typ = typ
        self.przebieg = przebieg
        self.kolor = kolor
        self.cena = cena

    def swiatlo(self, czas = " podczas jazdy nocą "):
        return "{}".format(self.marka) + czas + "automatycznie włącza i wyłącza światła mijania."
    def kamera(self, kamera = " kamera wideo "):
        return "Zainstalowana w {} {}".format(self.marka, self.model) +kamera+ " rejestruje znaki i wyświetla odpowiednie informacje w postaci symboli na wyświetlaczu kokpitu"
    def muzyka(self):
        return "{} modeli {} ma wgrane aplikacje z internetowymi odtwarzaczami muzyki.".format(self.marka, self.model)
    def jazda(self):
        return "Nawet z przebiegiem {} {} {} fajnie dię trzyma na drodze.".format(self.przebieg,self.marka,self.model)
    def jedzprosto(self,ile):
        return "{} {} jedzie prosto {} km.".format(self.kolor,self.marka,ile)
ferrari = car("Ferrari", 458, "kabriolet",12000 , "czerwony", "60 000 $")
opel = car("Opel","Astra", "sedan", 147391, "czarny", "9 000 $")
volvo = car("Volvo", "s90", "sedan", 90154, "szary", "34 750 $")
mercedes = car("Mercedes - Benz", "klasa E", "couple", 14000, "zielony", "65 000 $")
audi = car("Audi", "A4", "auto miejskie", 162400 , "brązowy", "7 300 $")
print(opel.jedzprosto(ile = input("Ile km jechać prosto?")))
print(volvo.swiatlo())
print(ferrari.swiatlo(" całodobowo "))
print(mercedes.muzyka())
print(audi.jazda())
print(audi.kamera(" mega kamerka "))
print(volvo.kamera())

