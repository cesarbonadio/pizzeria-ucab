from .baseInfo import baseSizes,baseIngredients
from .cliMsg import *

def setPizzaSize(pizza,selectedSize):
    for size in baseSizes:
        if size.abbr == selectedSize:
            pizza.changeSize(size)
            print("{0}{1}".format(sizeSelected,size.name))

def isValidSize(selectedSize):
    for size in baseSizes:
        if size.abbr == selectedSize:
            return True
    return False

def addPizzaIngredient(pizza,selectedIngredient,zone=0):
    for ingredient in baseIngredients:
        if ingredient.abbr == selectedIngredient:
            if pizza.divided:
                pizza.addIngredient(ingredient,zone)
            else:
                pizza.addIngredient(ingredient)
            print("{0}".format(ingredientAdded))
            return None
    print("{0}".format(ingredientNotAdded))


def deletePizzaIngredient(pizza,selectedIngredient,zone=0):
    if pizza.divided:
        ingredientsListIterate = pizza.ingredients[zone-1]
    else:
        ingredientsListIterate = pizza.ingredients
    for ingredient in ingredientsListIterate:
        if ingredient.abbr == selectedIngredient:
            if pizza.divided:
                pizza.deleteIngredient(ingredient,zone)
            else:
                pizza.deleteIngredient(ingredient)
            print("{0}{1}".format(ingredientDeleted,ingredient.name))
            return None
    print("{0}".format(ingredientNotDeleted))


def showBaseIngredients():
    print("{0}".format(ingredientOptionsInstructive))
    for ingredient in baseIngredients:
        print("{0} ({1}) -> {2}$".format(ingredient.name,ingredient.abbr,ingredient.cost))
    print("\n")


def showPizzaSizes():
    return "\nOpciones:\nTamaños:" + ' '.join([str(size.name+"("+size.abbr+")"+str(size.cost)+"$") for size in baseSizes])


def setPizzaIngredients(pizza,order):
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
                break
