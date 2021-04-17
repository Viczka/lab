class book():
    def __init__(self, tytul, autor, rok, typ, cena):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.typ = typ
        self.cena = cena

    def czytaj(self):
        return "Przeczytaj {} autora {}, ta książka jest fantastyczna.".format(self.tytul, self.autor)
    def wybierz(self):
        return "Które z wydawnictw {} najbardziej Ci się podoba?".format(self.autor)
    def sprzedaj(self):
        return "Sprzedaję wszystkike ksiązki z rodzaju - '{}', ponieważ już zostały przeczytane przezemnie.".format(self.typ)
    def kupuj(self):
       return "W końcu kupię swoją ulubioną książke. Po przecenie ona kosztuje tylko {}.".format(self.cena)
    def wydanie(self):
        return "{} była wydana w {}.".format(self.tytul, self.rok)
    def sortuj(self):
        return "Książki wydane do 2000 roku. są to {}".format(self.tytul)
list = []
list1 = []
list.append(book("„Władca pierścieni”", "J.R.R Tolkien", 1992 , "fantastyka", "18.99 pln"))
list.append(book("„Buszujący w zbożu”", "Jerome David Salinger", 1991 , "literatura piękna", "24.53 pln"))
list.append(book("„Harry Potter - seria", "J.K.Rowling", 1997, "literatura młodzezowa", "225.14 pln"))
list.append(book("„Duma i uprzedzenie”", "Jane Austen", 1813 , "klasyka", "15.49 pln"))
list.append(book("„Niewidzialne życie Addie LaRue”", "Victoria Schwab", 2020 , "fantastyka", "32.12 pln"))
print(list[0].czytaj())
print(list[1].wydanie())
print(list[2].wybierz())
print(list[3].kupuj())
print(list[4].sprzedaj())
for i in list:
    if self.rok < 2000:
        print("jjj", i.sortuj())
