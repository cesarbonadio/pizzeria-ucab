from classes.pizza import *
from classes.characteristic import Ingredient,Size
from classes.order import Order
from util.pizzaUtil import *
from util.cliMsg import *
from util.cliUtil import *


if __name__ == '__main__':
    print(welcomeTitle)
    order = Order()
    while True:
        print("Pizza número {0}".format(len(order.pizzas)+1))
        while True:
            sizeOption = input("{0}:".format(showPizzaSizes()))
            if not isValidSize(sizeOption):
                print("{0}".format(sizeSelectionError))
                continue
            zoneTopping = ynCliOption(zoneQuestion)
            zonesQuantity = int(input("{0}".format(zoneOptions))) if zoneTopping else 0
            pizza = pizzaFactory.getPizza(zoneTopping, zones = zonesQuantity)
            order.addPizza(pizza)
            setPizzaSize(pizza,sizeOption)
            setPizzaIngredients(pizza,order)
            pizza.showPizzaSummary()
            break
        continueOrder = ynCliOption(continueQuestion)
        if continueOrder:
            continue
        else:
            break
    order.showOrderSummary()
