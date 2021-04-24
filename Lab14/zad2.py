class zwierze:
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    def przedstaw_sie(self):
        print("Jestem zwierzakiem {}, mam {} lat oraz wazę {} kg.".format(self.nazwa,self.wiek,self.waga))

    def urodziny(self):
        self.wiek += 1


class kot(zwierze):
    def przedstaw_sie(self):
        print("Jestem kotkiem {}, mam {} lat oraz wazę {} kg.".format(self.nazwa,self.wiek,self.waga))


class pies(zwierze):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("A tak w ogóle to jestem fajnym pieskiem")


class ptak(zwierze):
    def __init__(self, nazwa, wiek, waga, kolor):
        super().__init__(nazwa, wiek, waga)
        self.kolor = kolor

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("Jako ptak mój kolor to {}".format(self.kolor))


def main():
    garfild = kot("Garfild", 3, 1.5)
    cynamon = pies("Cynamon", 1, 4.8)
    irel = ptak("Irel", 2.8, 0.950, "szary")
    jakis_zwierz = zwierze("Piorun", 6, 9)

    garfild.przedstaw_sie()
    cynamon.przedstaw_sie()
    jakis_zwierz.przedstaw_sie()

    irel.urodziny()
    irel.przedstaw_sie()


if __name__ == "__main__":
    main()
#Jestem kotkiem Garfild, mam 3 lat oraz wazę 1.5 kg.
#Jestem zwierzakiem Cynamon, mam 1 lat oraz wazę 4.8 kg.
#A tak w ogóle to jestem fajnym pieskiem
#Jestem zwierzakiem Piorun, mam 6 lat oraz wazę 9 kg.
#Jestem zwierzakiem Irel, mam 3.8 lat oraz wazę 0.95 kg.
#Jako ptak mój kolor to szary