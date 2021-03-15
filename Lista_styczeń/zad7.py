import datetime
import time
def date ():
    tab = ['1 - today',
           '2 - yesterday',
           '3 - tomorrow',
           '4 - birthday'
    ]
    for i in range(0,len(tab)):
        print(tab[i])
    x = input("What date do you want to see?(format: 1-4):")
    if x == 1:
        today = datetime.date.today()
        print("Today:", "{}.{}.{}".format(today.day, today.month, today.year))
    elif x == 2:
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        print("Yesterday was:", "{}.{}.{}".format(yesterday.day,yesterday.month,yesterday.year))
    elif x == 3:
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=+1)
        print("Tomorrow will be:", "{}.{}.{}".format(tomorrow.day, tomorrow.month, tomorrow.year))
    elif x == 4:
        birthday = input("When you were born?(format - dd.mm.rrrr):")
        print("Your happy day:",time.strftime("%A",time.strptime(birthday , "%d.%m.%Y")))
date()