from classes.pizza import Pizza
from classes.characteristic import Ingredient,Size
from classes.order import Order
from util.pizzaUtil import *


if __name__ == '__main__':
    print("\n\n********PIZZERIA UCAB********")
    order = Order()
    while True:
        pizza = Pizza()
        order.addPizza(pizza)
        print("Pizza número {0}".format(len(order.pizzas)))
        while True:
            sizeOption = input("\nOpciones:\nTamaños: {0}:".format(showPizzaSizes()))
            if setPizzaSize(pizza,sizeOption):
                showBaseIngredients()
                while True:
                    ingredient = input("Indique el ingrediente:")
                    if '-' in ingredient:
                        deletePizzaIngredient(pizza,ingredient.replace("-",""))
                        continue
                    elif ingredient != '':
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
