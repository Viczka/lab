def test():
    correct = []
    true = ['c','b','c','a','b','c','a','c','b','a','a']
    questions = ['1.Najważniejszym urządzeniem zestawu komputerowego jest:',
                 '2.Programy w systemie Windows uruchamiają się w postaci:',
                 '3.Folder przeznaczony do szybkiego zapisywania plików w systemie Windows to:',
                 '4.Czym jest zapisanie dokumentu:',
                 '5.Twardy dysk to:',
                 '6.Przycisk Start umożliwia:',
                 '7.Komputer będzie działał wtedy, gdy będzie w nim zainstalowany:',
                 '8.Pasek zadań znajduje się:',
                 '9.Skrót klawiszowy przeznaczony do zapisywania to:',
                 '10.Najważniejszą częścią elektroniczną , umieszczoną wewnątrz jednostki centalnej, nazywaną "mózgiem komputera" jest  :',
                 '11.* Plik to:']
    answers = ["""    a) klawiatura, 
    b) drukarka, 
    c) jednostka centralna""",
    """    a) paska
    b) okien 
    c) kartki""",
    """    a) kosz
    b) mój komputer
    c) moje dokumenty""",
    """    a) przekazanie informacji na dysk 
    b) przygotowanie dokumentu do druku
    c) wyjście z programu""",
    """    a) rodzaj drukarki
    b) pamięć komputera 
    c) program komputerowy""",
    """    a) drukowanie
    b) zapisywanie dokumentów
    c) uruchamianie programów zainstalowanych na komputerze""",
    """    a) system operacyjny 
    b) edytor tekstu
    c) program antywirusowy""",
    """    a) na dyskietce
    b) w folderze
    c) w dolnej części Pulpitu""",
    """    a) Alt + Z
    b) Ctrl + S
    c) Ctrl + Z""",
    """    a) procesor
    b) karta graficzna 
    c) modem""",
    """    a) zapisana w komputerze informacja 
    b) program komputerowy
    c) urządzenie znajdujące się wewnątrz jednostki centralnej"""]
    for i in range(0, len(true)):
        print(questions[i])
        print(answers[i])
        x = input("Twoja odpowiedź?:")
        if x == true[i]:
            correct.append(x)
    if len(correct) == 11:
        return "Ocena 'celująca' - 6"
    elif len(correct) >=8 and len(correct) <= 10:
        return "Ocena 'bardzo dobra' - 5"
    elif len(correct) == 6 or len(correct) == 7:
        return "Ocena 'dobra' - 4"
    elif len(correct) == 4 or len(correct) == 5:
        return "Ocena 'dostateczna' - 3"
    elif len(correct) == 2 or len(correct) == 3:
        return "Ocena 'dopuszczająca' - 2"
    else:return "Ocena 'negatywna' - 1"

def menu():
    x = input("Chcesz rozwiązać test? Odpowiedz 'tak' lub 'nie':").upper()
    if x == 'NIE':
        print("Szkoda =(")
    elif x == 'TAK':
        print('Nice =). To zaczynamy zabawe.'), print(test())
    else:print("Padałeś nie poprawną odpowiedź")
menu()

