import sqlite3
#! /usr/bin/env python3
#-*-coding: utf-8-*-
con = sqlite3.connect('user')
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.executescript("""
    DROP TABLE IF EXISTS contacts;
    CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY ASC,
    name varchar (250) NOT NULL,
    username varchar (250) NOT NULL,
    age INTEGER NOT NULL
    adres varchar (250) NOT NULL
    earnings INTEGER NOT NULL
    )""")


def update_program(self):
        cur = self.execute("SELECT * from contacts")
        for x in cur:
            temp = contacts(x[0], x[1], x[2], x[3])
            self.list.append(temp)

    def add_osobe(self, name):
        self.execute(
            f"""INSERT INTO contacta(name, username, age, adres, earnings) 
        VALUES('{contacts.name}','{contacts.username}','{contacts.age}','{contacts.adres}','{contacts.earnings})""")
        self.commit()
        self.list.append(contacts)

    def remove_osobe(self, contacts):
        for x in self.list:
            if x.name == contacts.name and x.username == contacts.username and x.age == contacts.age and x.adres == contacts.adres and x.earnings == contacts.earnings:
                self.execute(
                    f"""DELETE FROM contacts WHERE name = '{contacts.name}' AND username = '{contacts.username}' 
                    AND age = '{contacts.age}' AND adres = '{contacts.adres}' AND earnings = '{contacts.earnings}'""")
                self.commit()
        self.list = [x for x in self.list if
                           x.name != contacts.name and x.username != contacts.username and x.age != contacts.age and x.adres != contacts.adres and x.earnings != contacts.earnings]

    def sortowanie(self):
        templist = sorted(self.list, key=lambda contacts: contacts.username)
        for x in templist:
            print(f"{x.username} {x.name}; earnings = {x.earnings}")

    def zarobki_up(self):
        templist = sorted(self.list, key=lambda contacts: contacts.earnings)
        for x in templist:
            print(f"{x.username} zarabia {x.earnings}")

    def zarobki_down(self):
        templist = sorted(self.list, key=lambda contacts: contacts.earnings, reverse=True)
        for x in templist:
            print(f"{x.username} zarabia {x.earnings}")


class contacts:
    def __init__(self, name, username, age, adres, earnings):
        self.name = name
        self.username = username
        self.age = age
        self.adres = adres
        self.earnings = earnings

    def __repr__(self):
        return f"{self.username} from {self.adres} contacts {self.earnings}"

b1 = user()
cont = contacts("Vika", "Andrusyk", '21', "Ocice", 5445)
cont2 = contacts("dawid", "GHYD","22", "Wrocław", 5454)
b1.sortowanie()
b1.zarobki_up()
b1.zarobki_down()