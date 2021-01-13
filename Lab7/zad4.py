a = ('nie', 'chcę', 'mi','się', 'dziś', '.','pójdę','spać')
x = str(input("Wpisz jakieś słowo:"))
if x in a :
    print("Odpowiedź -", x in a,".","Krotka zawiera takie słowo pod indexem:", a.index(x))
    print("Słowo","'",x,"'", "występuje", a.count(x),"raz/y")
else:print("Odpowiedź -", x in a,".","Krotka nie zawiera takiego  słowa")

