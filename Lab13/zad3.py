import re
class smartfon():
    def __init__(self, producent, model,system_operacyjny, ekran, kolor):
        self.producent = producent
        self.model = model
        self.system_operacyjny = system_operacyjny
        self.ekran = ekran
        self.kolor=kolor
    def dzwon(self, numer = input("Podaj numer do którego chcesz zadzwonić(format: +48 ***-***-***): +48 ")):
        if re.search("\d{3}-\d{3}-\d{3}",numer):
            print("Numer poprawny.")
            return "Dzwonimy do +48 {}..".format(numer)
        else:return "Blędnie wprowadzony numer."

    def innykolor(self, inny_kolor = input("w jaki kolor malujemy telefon?")):
        if str.isalpha(inny_kolor) == True:
            return "{} ma {} kolor. Pomalujemy go na {}".format(self.model,self.kolor,inny_kolor)
        else:return "Blędnie wprowadzony kolor."
iphone = smartfon("Apple", "iPhone 6s","iOS 10","4.7 cali","czarny")
samsung = smartfon("Samsung","Samsung M21", "Android 10", "6.4 cali", "niebieski")
print(iphone.dzwon())
print(samsung.innykolor())




