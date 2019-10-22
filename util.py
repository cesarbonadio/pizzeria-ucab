from baseInfo import baseSizes,baseIngredients

def setPizzaSize(pizza,selectedSize):
    for size in baseSizes:
        if size.abbr == selectedSize:
            pizza.changeSize(size)
            print("\nTamaño seleccionado: {0}".format(size.name))
            return True
    return False

def setPizzaIngredient(pizza,selectedIngredient):
    for ingredient in baseIngredients:
        if ingredient.abbr == selectedIngredient:
            pizza.addIngredient(ingredient)
            return True
    return False

def showBaseIngredients():
    print("Ingredientes:")
    for ingredient in baseIngredients:
        print("{0} ({1})".format(ingredient.name,ingredient.abbr))
