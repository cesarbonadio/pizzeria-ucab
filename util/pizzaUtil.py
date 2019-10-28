"""
    Este módulo sirve de utilidad para las diferentes operaciones
    que se le pueden hacer a la pizza y no comunicarse directamente
    con la clase. Básicamente tiene funciones que ayudar a separar
    la lógica de la aplicación del ejecutable principal
"""

# Importar módulos necesarios
from .baseInfo import baseSizes,baseIngredients
from .cliMsg import *



def setPizzaSize(pizza,selectedSize):
    '''
        Elegir el tamaño de la pizza

        Parametros:
           :param Pizza pizza: La pizza a la cual se le va a setear el tamano
           :param str selectedSize: El nombre del tamano seleccionado

        :return: None
   '''
    for size in baseSizes:
        if size.abbr == selectedSize:
            pizza.changeSize(size)
            print("{0}{1}".format(sizeSelected,size.name))



def isValidSize(selectedSize):
    '''
        Chequear si el tamano seleccionado es valido

        Parametros:
           :param str selectedSize: El nombre del tamano seleccionado

        :return: boleano que dice si es un tamano valido o no
   '''
    for size in baseSizes:
        if size.abbr == selectedSize:
            return True
    return False



def addPizzaIngredient(pizza,selectedIngredient,zone=0):
    '''
        Elegir el tamaño de la pizza

        Parametros:
           :param Pizza pizza: La pizza a la cual se le va a agregar el ingrediente
           :param str selectedSize: El nombre del tamano seleccionado
           :param int zone: la zona a la cual se le va a agregar el ingrediente, si es 0 no es una pizza dividida

        :return: None
   '''
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
    '''
        Elegir el tamaño de la pizza

        Parametros:
           :param Pizza pizza: La pizza a la cual se le va a agregar el ingrediente
           :param str selectedSize: El nombre del tamano seleccionado
           :param int zone: la zona a la cual se le va a agregar el ingrediente, si es 0 no es una pizza dividida

        :return: None
   '''
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
    '''
        Elegir el tamaño de la pizza

        :return: None
   '''
    print("{0}".format(ingredientOptionsInstructive))
    for ingredient in baseIngredients:
        print("{0} ({1}) -> {2}$".format(ingredient.name,ingredient.abbr,ingredient.cost))
    print("\n")



def showPizzaSizes():
    '''
        Metodo que retorna un string para mostrar los tamanos disponibles.
        De forma que trabaje dinamicamente con los tamanos bases

        :return: str que tiene los tamanos base
   '''
    return "\nOpciones:\nTamaños:" + ' '.join([str(size.name+"("+size.abbr+")"+str(size.cost)+"$") for size in baseSizes])




def setPizzaIngredients(pizza,order):
    '''
        Elegir el tamaño de la pizza

        Parametros:
           :param Pizza pizza: La pizza a la cual se le va a agregar el ingrediente
           :param Order order: La orden que contiene todas las pizzas en memoria

        :return: None
   '''
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
