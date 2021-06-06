try:
    x=open("kodypocztowe.txt", "w")
    y=input("podaj polski kod pocztowy")
    if len(y)!=6 or y.isalpha() or y.isdigit():
        raise Exception("Bląd")
    if len(y)==6 and y[0].isdigit() and y[1].isdigit() and y[2]=="-" and y[3].isdigit() and y[4].isdigit() and y[5].isdigit():
        x.write(y)
except:
    print("Kod pocztowy nie zostal zapisany w pliku")
finally:
    x.close()
