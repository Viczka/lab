class Beer():
    def __init__(self,name,percentage,price, place_for_opinion):
        self.name = name
        self.percentage = percentage
        self.price = price
        self.place_for_opinion = place_for_opinion

    def __repr__(self):
        return f"Beer: {self.name} - price: {self.price}"

class Shop():
    def __init__(self, name):
        self.name = name

    fridge = []

    def buy(self):
        check = input("Are you 18 years old?")
        if check == 'no' or check == 'nie':
            print("We can't sell,sorry.")
        else: return self.sell(self.fridge)

    def sell(self, fridge):
        choice = str(input("What kind of beer do you want to buy: "))
        if choice in fridge:
            print('Supper')
        else:
            print("Soryy.")

    def sort_price(self):
        print(sorted(self.fridge, key=lambda Beer:Beer.price))


def main():
    zabka = Shop("Żabka")
    netto = Shop("Netoo")

    Warka = Beer("Warka", "0%",3.6,"spoko")
    Kustosz = Beer("Kustosz","4%",2.7,"polecam")
    Lomza = Beer("Lomza","3.5%",1.95, "nie polecam")

    zabka.fridge.append(Warka)
    zabka.fridge.append(Kustosz)
    netto.fridge.append(Lomza)

    print(zabka.fridge)
    zabka.buy()
    zabka.sort_price()


if __name__ == '__main__':
    main()