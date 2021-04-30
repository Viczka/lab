class Hotel:
    def __init__(self, ilosc_pokoi, ilosc_pieter):
        self.ilosc_pokoi = ilosc_pokoi
        self.ilosc_pieter = ilosc_pieter
        self.pokoje = []
        nr_pokoju = 1
        for nr_pietra in range(self.ilosc_pieter):
            for i in range(self.ilosc_pokoi):
                self.pokoje.append(Pokoj(nr_pokoju=nr_pokoju, nr_pietra=nr_pietra))
                nr_pokoju += 1

class Pokoj:
    def __init__(self, nr_pokoju, nr_pietra, osoba = None):
        self.nr_pokoju = nr_pokoju
        self.nr_pietra = nr_pietra
        self.osoba = osoba

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko