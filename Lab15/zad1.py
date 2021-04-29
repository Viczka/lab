class Restaurant:
    def __init__(self,name,specification,address, __NIP,REGON,open,close):
        self.name = name
        self.specification = specification
        self.address = address
        self.__NIP = __NIP
        self.REGON = REGON
        self.open = open
        self.close = close

class IceCreamStand(Restaurant):
    flavors = ['cream', 'strawberry', 'oreo', 'spaliatella', 'mango', 'chokolate', 'caramel', 'salt caramel','watermelon']
    flavors2 = []
    def __init__(self,name,specification,address,NIP,REGON,open,close,flavors):
        super().__init__(name,specification,address,NIP,REGON,open,close)
        self.flavors = flavors

    def about(self):
        print("Hello.")

    def available_flavors(self):
       print(f'Menu : {self.flavors}')

    def add_flavors(self):
        new_flavors = input("What flavor would you lika to add to the menu?: ")
        if new_flavors in self.flavors:
            print("This flavors is already here")
        else: self.flavors2.append(new_flavors)

class CoffeeShop(Restaurant):
    coffee = ['americano', 'latte', 'capiccino', 'espresso', 'bouble espresso']
    coffee2 = []
    def about(self):
        print("Enjoy your meal.")

    def __init__(self,name,specification,address,NIP,REGON,open,close,coffee):
        super().__init__(name,specification,address,NIP,REGON,open,close)
        self.coffe = coffee

    def available_coffee(self):
        print(f'Menu : {self.coffe}')

    def add_coffee(self):
        new_coffee = input("What coffee would you lika to add to the menu?: ")
        if new_coffee in self.coffe:
            print("This flavors is already here")
        else: self.coffee2.append(new_coffee)

def main():
    for i in (IceCreamStand,CoffeeShop):
        i.about(CoffeeShop)

    ice = IceCreamStand("ICECREAM", "restaurant",'Wrocław',8907654,78656678,'12:00','20:00', IceCreamStand.flavors)
    coffee = CoffeeShop("Coffee",'ccoffe','Wrocław',7897657,86545678,'10:00','17:30',CoffeeShop.coffee)

    ice.available_flavors()
    ice.add_flavors()
    coffee.available_coffee()
    coffee.add_coffee()
    print(ice.name, ice.address, ice.REGON)
    print(ice.__NIP) #wyskoczy bląd ponieważ NIP jest niewidoczny dla uzytkownika


if __name__ == '__main__':
    main()