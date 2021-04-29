class Obywatel:
    def __init__(self, imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc

    def plik(self):
        print("----------------------\n{} {}\nul.{} {}\n{} {}\n----------------------\n".format(self.imie, self.nazwisko, self.ulica, self.nr_domu, self.kod_pocztowy, self.miejscowosc))

        plik = open("wizytowki.txt", "w")
        plik.write("Wizytowka - {} {}".format(self.imie,self.nazwisko))
        plik.close()

        obywatel = Obywatel("Jan", "Kowalski", "Rakowiecka", "20", "00-001", "Warszawa")
        obywatel.plik()

#----------------------
#Jan Kowalski
#ul.Rakowiecka 20
#00-001 Warszawa
#----------------------