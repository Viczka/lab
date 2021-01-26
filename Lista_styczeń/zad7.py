import datetime
import time
tab = {
    'today' : '1',
    'yesterday': '2',
    'tomorrow' : '3',
    'birthday': '4'
}
y = 1
for keys in tab.keys():
    print(y,'-',keys)
    y += 1
x = input("What date do you want to see?(format: 1-4):")
if x == tab['today']:
    today = datetime.date.today()
    print("Today:", "{}.{}.{}".format(today.day, today.month, today.year))
elif x == tab['yesterday']:
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    print("Yesterday was:", "{}.{}.{}".format(yesterday.day,yesterday.month,yesterday.year))
elif x == tab['tomorrow']:
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=+1)
    print("Tomorrow will be:", "{}.{}.{}".format(tomorrow.day, tomorrow.month, tomorrow.year))
elif x == tab['birthday']:
    birthday = input("When you were born?(format - dd.mm.rrrr):")
    print("Your happy day:",time.strftime("%A",time.strptime(birthday , "%d.%m.%Y")))
