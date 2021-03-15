class car():
    species = "smochód"
    def __init__(self, marka, model, typ, przebieg, kolor, cena):
        self.marka = marka
        self.model = model
        self.typ = typ
        self.przebieg = przebieg
        self.kolor = kolor
        self.cena = cena

    def swiatlo(self):
        return "{} podczas jazdy nocą automatycznie włącza i wyłącza światła mijania.".format(self.marka)
    def kamera(self):
        return "Zainstalowana w {} {} kamera wideo rejestruje znaki i wyświetla odpowiednie informacje w postaci symboli na wyświetlaczu kokpitu".format(self.marka, self.model)
    def muzyka(self):
        return "{} modeli {} ma wgrane aplikacje z internetowymi odtwarzaczami muzyki.".format(self.marka, self.model)
    def jazda(self):
        return "Nawet z przebiegiem {} {} {} fajnie dię trzyma na drodze.".format(self.przebieg,self.marka,self.model)
    def jedzprosto(self):
        return "{} {} jedzie prosto tak samo jak i inne samochody.".format(self.kolor,self.marka)
ferrari = car("Ferrari", 458, "kabriolet", "12 000 km", "czerwony", "60 000 $")
opel = car("Opel","Astra", "sedan", "147 391 km", "czarny", "9 000 $")
volvo = car("Volvo", "s90", "sedan", "90 154 km", "szary", "34 750 $")
mercedes = car("Mercedes - Benz", "klasa E", "couple", "14 000 km", "zielony", "65 000 $")
audi = car("Audi", "A4", "auto miejskie", "162 400 km", "brązowy", "7 300 $")
print(volvo.swiatlo())
print(ferrari.kamera())
print(mercedes.muzyka())
print(audi.jazda())
print(opel.jedzprosto())
