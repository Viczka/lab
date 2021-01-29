def baht ():
        y = float(input("Podaj ilość (THB):"))
        usd = y * 0.033357
        y1 = float(input("Podaj ilość (USD):"))
        thb = y1 * 29.9862
        print(y ,'(THB) -',"{:.2f}".format(usd),'(USD)')
        print(y1 ,'(USD) -',"{:.2f}".format(thb),'(THB)')
def bitcoin ():
        y = float(input("Podaj ilość (BTC):"))
        usd = y * 30404
        y1 = float(input("Podaj ilość (USD):"))
        btc = y1 * 0.00003289
        print(y, '(BTC) -', "{:.2f}".format(usd), '(USD)')
        print(y1, '(USD) -', "{:.6f}".format(btc), '(BTC)')
def ngultrum ():
        y = float(input("Podaj ilość (BTN):"))
        usd = y *  0.01372
        y1 = float(input("Podaj ilość (USD):"))
        btn = y1 * 72.8926
        print(y, '(BTN) -', "{:.2f}".format(usd), '(USD)')
        print(y1, '(USD) -', "{:.2f}".format(btn), '(BTN)')
def ugija ():
        y = float(input("Podaj ilość (MRO):"))
        usd = y * 0.00281
        y1 = float(input("Podaj ilość (USD):"))
        mro = y1 * 354.96
        print(y, '(MRO) -', "{:.2f}".format(usd), '(USD)')
        print(y1, '(USD) -', "{:.2f}".format(mro), '(MRO)')
def ethereum ():
        y = float(input("Podaj ilość (ETH):"))
        usd = y * 1308.21
        y1 = float(input("Podaj ilość (USD):"))
        eth = y1 * 0.00076440
        print(y, '(ETH) -', "{:.2f}".format(usd), '(USD)')
        print(y1, '(USD) -', "{:.5f}".format(eth), '(ETH)')
def dinar ():
        y = float(input("Podaj ilość (KWD):"))
        usd = y * 3.3031
        y1 = float(input("Podaj ilość (USD):"))
        kwd = y1 * 0.3027
        print(y, '(KWD) -', "{:.2f}".format(usd), '(USD)')
        print(y1, '(USD) -', "{:.2f}".format(kwd), '(KWD)')
def rial ():
        y = float(input("Podaj ilość (OMR):"))
        usd = y * 2.6005
        y1 = float(input("Podaj ilość (USD):"))
        omr = y1 * 0.3845
        print(y, '(OMR) -', "{:.2f}".format(usd), '(USD)')
        print(y1, '(USD) -', "{:.2f}".format(omr), '(OMR)')
def menu ():
    money = {
    '1': 'Baht Tajski(THB) - Dolary amerykańskie (USD)',
    '2': 'Bitcoin(BTC) - Dolary amerykański(USD)',
    '3': 'Ngultrum bhutański(BTN) - Dolary amerykańskie(USD)',
    '4': 'Ugija mauretańska(MRO) - Dolary amerykańskie (USD)',
    '5': 'Ethereum(ETH) – Dolary amerykańskie (USD)',
    '6': 'Dinar kuwejcki(KWD) - Dolary amerykańskie (USD)',
    '7': 'Rial omański(OMR) - Dolary amerykańskie (USD)'
    }
    y = 1
    for kasa in money.values():
        print(y,'-', kasa)
        y += 1
    x = int(input("Jak chcesz przeliczyć z podanych walut? Podaj numer:"))
    if x == 1: print(baht())
    elif x == 2: print(bitcoin())
    elif x == 3: print(ngultrum())
    elif x == 4: print(ugija())
    elif x == 5: print(ethereum())
    elif x == 6: print(dinar())
    elif x == 7: print(rial())
    else:print("Niema takiej pozycji.")
menu()
