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
            validSize = isValidSize(sizeOption)
            if not validSize:
                print("{0}".format(sizeSelectionError))
                continue
            zoneTopping = input("{0}".format(zoneQuestion))
            zonesQuantity = int(input("{0}".format(zoneOptions))) if zoneTopping.lower()=="s" else 0
            pizza = pizzaFactory.getPizza(zoneTopping, zones = zonesQuantity)
            order.addPizza(pizza)
            setPizzaSize(pizza,sizeOption)

            for zone in range (1,pizza.zones+1):
                if pizza.divided:
                    print("\nToppings pizza {0} - zona {1}".format(len(order.pizzas),zone))
                showBaseIngredients()
                while True:
                    ingredient = input("{0}".format(inputIngredient))
                    if '-' in ingredient:
                        deletePizzaIngredient(pizza,ingredient.replace("-",""),zone)
                    elif ingredient != '':
                        addPizzaIngredient(pizza,ingredient,zone)
                    else:
                        pizza.showPizzaSummary()
                        break
            break
        continueOrder = input("{0}".format(continueQuestion))
        if continueOrder.lower() == "n": break

    order.showOrderSummary()
