import smtplib
serniczkowy_spam = {}
a = 'tak'
b = 'nie'
x = input("Chcesz otrzymać fajne zdj.?Daj odpowiedź 'tak' lub 'nie':")
if x == a:
    imie = input("Podaj imie:")
    mail = input("Podaj mail:")
    serniczkowy_spam[imie] = mail
    print(serniczkowy_spam)
else: print("Nie to nie. Nara")
sender = 'viktoriaandrusik@gmail.com'
receivers = [serniczkowy_spam.values()]

