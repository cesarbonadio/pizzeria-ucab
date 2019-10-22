from characteristic import Size

class Pizza:

    def __init__(self):
        self.ingredients = []
        self.size = None
        self.total = 0

    def addIngredient(self,ingredient):
        self.ingredients.append(ingredient)
        self.total += ingredient.cost

    def changeSize(self,size):
        self.size = size
        self.total += size.cost

    def showPizza(self):
        print([x.name for x in self.ingredients])
        print(self.size.name) if self.size != None else print("No tiene tamaño asignado")

    def showPizzaSummary(self):
        if len(self.ingredients)>0:
            print("\n\nUsted seleccionó una pizza {0} con: {1}"
            .format(self.size.name,','.join([ingredient.name for ingredient in self.ingredients])))
        else:
            print("\n\nUsted seleccionó una pizza margarita (básica) {0}"
            .format(self.size.name))
        print("Subtotal a pagar por una pizza {0}: {1}".format(self.size.name,self.total))
