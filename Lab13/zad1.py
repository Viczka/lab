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
        return "{} podczas jazdy nocą automatycznie włącza i wyłącza światła mijania".format(self.marka)
    def

ferrari = car("Ferrari", 458, "kabriolet", "12 000 km", "czerwony", "60 000 $")
opel = car("Opel","Astra", "sedan", "147 391 km", "czarny", "9 000 $")
volvo = car("Volvo", "s90", "sedan", "90 154 km", "szary", "34 750 $")
mercedes = car("Mercedes - Benz", "klasa E", "couple", "14 000 km", "zielony", "65 000 $")
audi = car("Audi", "A4", "auto miejskie", "162 400 km", "brązowy", "7 300 $")
print(opel.swiatlo())