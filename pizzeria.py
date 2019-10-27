from classes.pizza import *
from classes.characteristic import Ingredient,Size
from classes.order import Order
from util.pizzaUtil import *
from util.cliMsg import *


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
            zoneTopping = input("{0}".format(zoneQuestion))
            zonesQuantity = int(input("{0}".format(zoneOptions))) if zoneTopping.lower()=="s" else 0
            pizza = pizzaFactory.getPizza(zoneTopping, zones = zonesQuantity)
            order.addPizza(pizza)
            setPizzaSize(pizza,sizeOption)
            setPizzaIngredients(pizza,order)
            pizza.showPizzaSummary()
            break
        continueOrder = input("{0}".format(continueQuestion))
        if continueOrder.lower() == "n": break
    order.showOrderSummary()
