class pojazd():
   def __init__ (self,marka, nr_tablicy):
      self.marka = marka
      self.nr_tablicy = nr_tablicy

   def jedz(self):
        print("Tu {}. Jedzie prosto i nawet skręca w prawo i w lewo.".format(self.marka))

class samochod(pojazd):
    def cofaj(self):
        super().jedz()
        print("A tak ogólnie to nawet cofa do tyłu.")

class motocykl(pojazd):
    def __init__(self,nr_tabicy,predkosc):
        super().__init__("honda",nr_tabicy)
        self.predkosc = predkosc

    def stoj(self):
        print("masakra co tu się dzieje, on ma numer",self.nr_tablicy,"i jedzie z prędkością",self.predkosc)

def main ():
    audi = samochod('audi', "GH678O")
    honda = motocykl("YJ90O", 142)

    honda.stoj()
    honda.jedz()
    audi.cofaj()
    print(audi.marka)

if __name__ == '__main__':
    main()
#masakra co tu się dzieje, on ma numer YJ90O i jedzie z prędkością 143
#Tu honda. Jedzie prosto i nawet skręca w prawo i w lewo.
#Tu audi. Jedzie prosto i nawet skręca w prawo i w lewo.
#A tak ogólnie to nawet cofa do tyłu.
#audi