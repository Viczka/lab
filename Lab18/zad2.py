with open("pantadeusz.txt", encoding="utf-8") as plik:
    for i, line in enumerate(plik):
        if i==7:
            print(line.readline()[7])
        elif i==11:
            print(line.readline()[11])
        if i==59:
            print(line.readline()[59])
        if i==97:
            print(line.readline()[97])
        if i==103:
            print(line.readline()[103])
