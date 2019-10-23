from classes.pizza import *
from classes.characteristic import Ingredient,Size
from classes.order import Order
from util.pizzaUtil import *


if __name__ == '__main__':
    print("\n\n********PIZZERIA UCAB********")
    order = Order()
    while True:
        print("Pizza número {0}".format(len(order.pizzas)+1))
        while True:
            sizeOption = input("{0}:".format(showPizzaSizes()))
            zoneTopping = input("{0}".format(showZoneQuestion()))
            if zoneTopping.lower()=="s":
                zonesQuantity = int(input("{0}".format(showZoneOptions())))
            else:
                zonesQuantity = 0
            pizza = pizzaFactory.getPizza(zoneTopping, zones = zonesQuantity)
            order.addPizza(pizza)
            if setPizzaSize(pizza,sizeOption):
                for zone in range (1,pizza.zones+1):
                    if pizza.divided:
                        print("\n Eligiendo los ingredientes de la pizza {0} - zona {1}".format(len(order.pizzas),zone))
                    showBaseIngredients()
                    while True:
                        ingredient = input("Indique el ingrediente:")
                        if '-' in ingredient:
                            if pizza.divided:
                                deletePizzaIngredient(pizza,ingredient.replace("-",""),zone)
                            else:
                                deletePizzaIngredient(pizza,ingredient.replace("-",""))
                            continue
                        elif ingredient != '':
                            if pizza.divided:
                                addPizzaIngredient(pizza,ingredient,zone)
                            else:
                                addPizzaIngredient(pizza,ingredient)
                            continue
                        else:
                            pizza.showPizzaSummary()
                            break
                break
            else:
                print("\n\nPorfavor indique un tamaño válido")
                continue
        continueOrder = input("\n¿Desea continuar?[s/n]:")
        if continueOrder.lower() == "s":
            continue
        elif continueOrder.lower() == "n":
            break
    order.showOrderSummary()
