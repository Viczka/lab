def test():
    true = []
    question1 = input("""1.Najważniejszym urządzeniem zestawu komputerowego jest: 
    a) klawiatura
    b) drukarka
    c) jednostka centralna
    Twoja odpowiedź?:""")
    if question1 == 'c':
        true.append(question1)
    question2 = input("""2.Programy w systemie Windows uruchamiają się w postaci:
    a) paska
    b) okien 
    c) kartki
    Twoja odpowiedź?:""")
    if question2 == 'b':
        true.append(question2)
    question3 = input("""3.Folder przeznaczony do szybkiego zapisywania plików w systemie Windows to:
    a) kosz
    b) mój komputer
    c) moje dokumenty
    Twoja odpowiedź?:""")
    if question3 == 'c':
        true.append(question3)
    question4 = input("""4.Czym jest zapisanie dokumentu:
    a) przekazanie informacji na dysk 
    b) przygotowanie dokumentu do druku
    c) wyjście z programu
    Twoja odpowiedź?:""")
    if question4 == 'a':
        true.append(question4)
    question5 = input("""5.Twardy dysk to:
    a) rodzaj drukarki
    b) pamięć komputera 
    c) program komputerowy
    Twoja odpowiedź?:""")
    if question5 == 'b':
        true.append(question5)
    question6 = input("""6.Przycisk Start umożliwia:
    a) drukowanie
    b) zapisywanie dokumentów
    c) uruchamianie programów zainstalowanych na komputerze
    Twoja odpowiedź?:""")
    if question6 == 'c':
        true.append(question6)
    question7 = input("""7.Komputer będzie działał wtedy, gdy będzie w nim zainstalowany:
    a) system operacyjny 
    b) edytor tekstu
    c) program antywirusowy
    Twoja odpowiedź?:""")
    if question7 == 'a':
        true.append(question7)
    question8 = input("""8.Pasek zadań znajduje się:
    a) na dyskietce
    b) w folderze
    c) w dolnej części Pulpitu
    Twoja odpowiedź?:""")
    if question8 == 'c':
        true.append(question8)
    question9 = input("""9.Skrót klawiszowy przeznaczony do zapisywania to :
    a) Alt + Z
    b) Ctrl + S
    c) Ctrl + Z
    Twoja odpowiedź?:""")
    if question9 == 'b':
        true.append(question9)
    question10 = input("""10.Najważniejszą częścią elektroniczną , umieszczoną wewnątrz jednostki centalnej, nazywaną "mózgiem komputera" jest  :
    a) procesor
    b) karta graficzna 
    c) modem
    Twoja odpowiedź?:""")
    if question10 == 'a':
        true.append(question10)
    question11 = input("""11.* Plik to:
    a) zapisana w komputerze informacja 
    b) program komputerowy
    c) urządzenie znajdujące się wewnątrz jednostki centralnej
    Twoja odpowiedź?:""")
    if question11 == 'a':
        true.append(question11)
    if len(true) == 0 or len(true) == 1:
        return "Ocena 'negatywna' - 1"
    if len(true) == 2 or len(true) == 3 :
        return "Ocena 'dopuszczająca' - 2"
    if len(true) == 4 or len(true) == 5:
        return "Ocena 'dostateczna' - 3"
    if len(true) ==6 or len(true) == 7:
        return "Ocena 'dobra' - 4"
    if len(true) >=8 and len(true) <= 10:
        return "Ocena 'bardzo dobra' - 5"
    if len(true) == 11:
        return "Ocena 'celująca' - 6"

def menu():
    x = input("Chcesz rozwiązać test? Odpowiedz 'tak' lub 'nie':")
    if x == 'nie':
        print("Szkoda =(")
    elif x == 'tak':
        print('Nice =). To zaczynamy zabawe.'), print(test())
    else:print("Padałeś nie poprawną odpowiedź")
menu()

