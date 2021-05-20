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
    )""")

cur.executescript("""
    DROP TABLE IF EXISTS numberphone;
    CREATE TABLE IF NOT EXISTS numberphone(
    id INTEGER PRIMARY KEY ASC,
    numberphone INTEGER NOT NULL,
    email varchar (250) NOT NULL,
    contacts_id INTEGER NOT NULL,
    FOREIGN KEY(contacts_id) REFERENCES contacts(id)
    )""")

cur.execute('INSERT INTO contacts VALUES(NULL,?,?,?);',('Viktoriia','Andrusyk','21'))
cur.execute('INSERT INTO contacts VALUES(NULL,?,?,?);',('Patryk','Jasiński','19'))
cur.execute('INSERT INTO contacts VALUES(NULL,?,?,?);',('Dawid','Biegacz','23'))

cur.execute('INSERT INTO numberphone VALUES(NULL,?,?,?);',('508605301','vika@gmail.com','1'))
cur.execute('INSERT INTO numberphone VALUES(NULL,?,?,?);',('796446262','patryk@wp.pl','2'))
cur.execute('INSERT INTO numberphone VALUES(NULL,?,?,?);',('609892361','dawid@gmail.com','3'))

con.commit()

def readdate():
        with con:
            cur.execute('SELECT * FROM contacts')
            conclusion_contacts = cur.fetchall()
            print('\n Contacts: ')
            for x in conclusion_contacts:
                print(x['id'],x['name'],x['username'],x['age'])

            cur.execute('SELECT * FROM numberphone, contacts WHERE numberphone.contacts_id = contacts.id')
            conclusion_numperphone = cur.fetchall()
            print('\n Number Phone: ')
            for x in conclusion_numperphone:
                print(x['id'],x['name'],x['numberphone'],x['email'])
readdate()
con.close()
