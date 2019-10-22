from pizza import Pizza
from characteristic import Ingredient,Size
from order import Order
from util import *


if __name__ == '__main__':
    print("\n\n********PIZZERIA UCAB********")
    order = Order()

    while True:
        pizza = Pizza()
        order.addPizza(pizza)
        print("Pizza numero {0}".format(len(order.pizzas)))
        while True:
            sizeOption = input("\nOpciones:\nTamaños: Grande(g) Mediana(m) Personal(p): ")
            if setPizzaSize(pizza,sizeOption):
                showBaseIngredients()
                while True:
                    ingredient = input("indique ingrediente (enter para terminar):")
                    if ingredient != '':
                        setPizzaIngredient(pizza,ingredient)
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
