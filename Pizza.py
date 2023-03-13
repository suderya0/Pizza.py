from csv import writer
import time


class Pizza:
    def __init__(self, description, price, number):
        self.description = description
        self.price = price
        self.number = number

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price

        # Sub Classes


class Classic(Pizza):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class Margherita(Pizza):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class Turk(Pizza):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class Plain(Pizza):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


# Objects of the  Pizzas subclasses
classic = Classic("Classic pizza.", 50, 1)
marg = Margherita("Margherita pizza.", 60, 2)
turk = Turk("Turk pizza.", 70, 3)
plain = Plain("Plain pizza", 40, 4)


# Decorator Classes
class Decorators(Pizza):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)
        self.component = None

    def get_cost(self):
        return self.component.get_cost() + \
               Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
               Pizza.get_description(self)


# Sub Classes
class Olives(Decorators):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class Mushrooms(Decorators):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class GoatCheese(Decorators):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class Meat(Decorators):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class Onions(Decorators):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


class Corn(Decorators):
    def __init__(self, description, price, number):
        super().__init__(description, price, number)


# Object of the Decorators subclasses
olive = Olives("Olive", 5, 5)
mushroom = Mushrooms("Mushrooms", 8, 6)
Goat_Cheese = GoatCheese("Goat Cheese", 12, 7)
meat = Meat("Meat", 10, 8)
onions = Onions("Onions", 3, 9)
corn = Corn("Corn", 2, 10)


def main():
    with open("Menu.txt", "r") as menu:
        print(menu.read())

    pizzaNumber = int(input("Please write the number of your pizza: "))
    pizzaCost = 0
    pizzaDescription = None

    sauceNumber = int(input("Please write the number of your sauce: "))
    sauceCost = 0
    sauceDescription = None

    if pizzaNumber == classic.number:
        pizzaCost = classic.get_cost()
        pizzaDescription = classic.get_description()
    elif pizzaNumber == turk.number:
        pizzaCost = turk.get_cost()
        pizzaDescription = turk.get_description()
    elif pizzaNumber == marg.number:
        pizzaCost = marg.get_cost()
        pizzaDescription = marg.get_description()
    elif pizzaNumber == plain.number:
        pizzaCost = plain.get_cost()
        pizzaDescription = plain.get_description()
    else:
        print("Only 1, 2, 3 and 4 please.")

    if sauceNumber == olive.number:
        sauceCost = olive.price
        sauceDescription = olive.description
    elif sauceNumber == mushroom.number:
        sauceCost = mushroom.price
        sauceDescription = mushroom.description

    elif sauceNumber == Goat_Cheese.number:
        sauceCost = Goat_Cheese.price
        sauceDescription = Goat_Cheese.description

    elif sauceNumber == meat.number:
        sauceCost = meat.price
        sauceDescription = meat.description

    elif sauceNumber == onions.number:
        sauceCost = onions.price
        sauceDescription = onions.description

    elif sauceNumber == corn.number:
        sauceCost = corn.price
        sauceDescription = corn.description

    else:
        print("Only 5, 6, 7, 8, 9 and 10 please.")

    name = input("Please enter your name: ")
    tckn = input("Please enter your user ID: ")
    creditCardNumber = int(input("Please enter your Credit Card number: "))
    creditCardPassword = input("Please enter your password: ")
    timeNow = time.localtime()
    currentTime = time.strftime("%H:%M:%S", timeNow)
    informations = [f"Name: {name} ,TCKN: {tckn}, Credit Card Number: {creditCardNumber} ,"
                    f" Credit Card Password: {creditCardPassword}, Time: {currentTime}"]
    pizzaDetail = [f"Pizza Base is: {pizzaDescription}, Sauce is: {sauceDescription} "
                   f" Cost: {pizzaCost + sauceCost}$"]
    with open("Orders_Database.csv", "w") as file:

        csv_writer = writer(file)
        csv_writer.writerow(informations)
        csv_writer.writerow(pizzaDetail)
    print("Thanks for choosing us. Enjoy your meal :)")


main()