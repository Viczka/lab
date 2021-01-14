import webbrowser
date = {
    'viktoria123': '1111',
    'pączek': '2222',
    'admin': 'admin',
    'choinka1': '3333',
    'jaśmin67': '4444',
    'dinxu': '5555'
}
login = input("podaj login:")
passw = input("podaj hasło:")
if login in date.keys() and passw in date.values():
    print("Świetnie. Udało Ci się")
    if login == 'admin' and passw == 'admin':
        webbrowser.open('admin.html')
    else:webbrowser.open('users.html')
else:print("Niepoprawnie wprowadzone login lub hasło")

