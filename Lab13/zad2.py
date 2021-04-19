class book():
    def __init__(self, tytul, autor, rok, typ, cena):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.typ = typ
        self.cena = cena
    def czytaj(self, opis = 'fantastyczna'):
        x = str(input("Jakie rodzaje książek lubisz (fantastyka, klasyka, literatura piękna, literatura młodzieżowa)?"))
        if x == 'fantastyka':
            return "Przeczytaj {} autora {}, ta książka jest".format(list[0].tytul, list[0].autor) + opis + "oraz {} {}.".format(list[4].tytul, list[4].autor)
        if x == 'klasyka':
            return "Przeczytaj {} autora {}, ta książka jest".format(list[3].tytul, list[3].autor) + opis
        if x == 'literatura młodzieżowa':
            return "Przeczytaj {} autora {}, ta książka jest".format(list[2].tytul, list[2].autor) + opis
        if x == 'literatura piękna':
            return "Przeczytaj {} autora {}, ta książka jest".format(list[1].tytul, list[1].autor) + opis
    def wybierz(self):
        return "Które z wydawnictw {} najbardziej Ci się podoba?".format(self.autor)
    def sprzedaj(self):
        return "Sprzedaję wszystkike ksiązki z rodzaju - '{}', ponieważ już zostały przeczytane przezemnie.".format(self.typ)
    def kupuj(self, cena= input("Ile kosztuje książka?:")):
       return "Teraz mozesz kupić książke {}. Po przecenie ona kosztuje tylko ".format(self.tytul) + cena + " pln.."
    def wydanie(self):
        return "{} była wydana w {}.".format(self.tytul, self.rok)
    def sortuj(self):
        return "Książki wydane do 2000 roku. są to {}".format(self.tytul)
list = []
list.append(book("„Władca pierścieni”", "J.R.R Tolkien", 1992 , "fantastyka", "18.99 pln"))
list.append(book("„Buszujący w zbożu”", "Jerome David Salinger", 1991 , "literatura piękna", "24.53 pln"))
list.append(book("„Harry Potter - seria", "J.K.Rowling", 1997, "literatura młodzieżowa", "225.14 pln"))
list.append(book("„Duma i uprzedzenie”", "Jane Austen", 1813 , "klasyka", "15.49 pln"))
list.append(book("„Niewidzialne życie Addie LaRue”", "Victoria Schwab", 2020 , "fantastyka", "32.12 pln"))
print(list[3].kupuj())
print(list[0].czytaj(" bardzo ciekawa."))
print(list[1].wydanie())
print(list[2].wybierz())
print(list[4].sprzedaj())

