from .baseInfo import baseSizes,baseIngredients

def setPizzaSize(pizza,selectedSize):
    for size in baseSizes:
        if size.abbr == selectedSize:
            pizza.changeSize(size)
            print("\nTamaño seleccionado: {0}".format(size.name))
            return True
    return False

def addPizzaIngredient(pizza,selectedIngredient):
    for ingredient in baseIngredients:
        if ingredient.abbr == selectedIngredient:
            pizza.addIngredient(ingredient)
            print("Ingrediente agregado")
            return None
    print("Ingrediente inválido")

def deletePizzaIngredient(pizza,selectedIngredient):
    for ingredient in pizza.ingredients:
        if ingredient.abbr == selectedIngredient:
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
    return ' '.join([str(size.name+"("+size.abbr+")"+str(size.cost)+"$") for size in baseSizes])
