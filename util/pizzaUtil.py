from .baseInfo import baseSizes,baseIngredients

def setPizzaSize(pizza,selectedSize):
    for size in baseSizes:
        if size.abbr == selectedSize:
            pizza.changeSize(size)
            print("\nTamaño seleccionado: {0}".format(size.name))
            return True
    return False


def addPizzaIngredient(pizza,selectedIngredient,zone=0):
    for ingredient in baseIngredients:
        if ingredient.abbr == selectedIngredient:
            if zone > 0:
                pizza.addIngredient(ingredient,zone)
            else:
                pizza.addIngredient(ingredient)
            print("Ingrediente agregado")
            return None
    print("Ingrediente inválido")


def deletePizzaIngredient(pizza,selectedIngredient,zone=0):
    if zone == 0:
        ingredientsListIterate = pizza.ingredients
    else:
        ingredientsListIterate = pizza.ingredients[zone-1]
    for ingredient in ingredientsListIterate:
        if ingredient.abbr == selectedIngredient:
            if zone > 0:
                pizza.deleteIngredient(ingredient,zone)
            else:
                pizza.deleteIngredient(ingredient)
            print("Un topping de {0} eliminado".format(ingredient.name))
            return None
    print("No se eliminó el topping está agregado a la pizza o no existe")


def showBaseIngredients():
    print("\n\nA continuación se le presentan la lista de los ingredientes: \n" \
    "Presione enter si quiere dejar de introducir ingrediente \n" \
    "Escriba - antes del ingrediente si quiere eliminar un ingrediente. Ej: -ja")
    for ingredient in baseIngredients:
        print("{0} ({1}) -> {2}$".format(ingredient.name,ingredient.abbr,ingredient.cost))
    print("\n")


def showPizzaSizes():
    return "\nOpciones:\nTamaños:" + ' '.join([str(size.name+"("+size.abbr+")"+str(size.cost)+"$") for size in baseSizes])


def showZoneQuestion():
    return "\n¿Quiere separar los toppings de la pizza por areas?[s/n]:"


def showZoneOptions():
    return "Seleccionar la cantidad de zonas en las que se dividirá la pizza (max 4):"
