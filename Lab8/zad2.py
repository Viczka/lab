contacts = {
    "Viczka" : 508605301,
    "Rostyk" : 675384901,
    "Adam" : 785622834,
    "Patryk" : 758347588,
    "Filip" : 887123401,
    "Angelika" : 870012345,
    "Natalia" : 901374810,
    "Kornelia" : 174503945,
    "Dawid" : 980345812,
    "Justyna" : 675829388
}
print(contacts)
contacts["Viczka"] = 478298743
contacts["Dawid"] = 989876574
print(contacts)
contacts.clear()
while len(contacts) != 2:
    name = input("Podaj imie:")
    number = input("Podaj numer tel.:")
    contacts[name] = number
    print(contacts)
print(sorted(contacts))

