class student():
    def __init__(self, imie, index, kierunek, rok):
        self.imie = imie
        self.index = index
        self.kiekunek = kierunek
        self.rok = rok
    def studia(self):
        return "{} studijuje na kierunku {}.".format(self.imie,self.kiekunek)
    def nik(self, nowy_index = input("Jak chcesz żeby do Ciebie się zwracali? ")):
        if str.isalpha(nowy_index) == True:
            return "Czuję się robotem z numerem indexu {}, mogli by mówić po prostu {}.".format(self.index, str.capitalize(nowy_index))
        else: return "{} - taki index mi pasuje."
student1 = student("Viktoriia", "43406", "Informatyka", "1")
student2 = student("Paweł", "14572","Hotelarstwo", "3")
student3 = student("Kasia", "67877", "Gastronomia", "2")
print(student1.nik())
print(student2.studia())
