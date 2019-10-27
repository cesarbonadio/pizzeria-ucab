from .characteristic import Size
from util.cliMsg import *

class Pizza:

    def __init__(self):
        self.ingredients = []
        self.size = None
        self.total = 0
        self.zones = 1
        self.divided = False

    def addIngredient(self,ingredient):
        self.ingredients.append(ingredient)
        self.total += ingredient.cost


    def deleteIngredient(self,ingredient):
        self.ingredients.remove(ingredient)
        self.total -= ingredient.cost


    def changeSize(self,size):
        self.size = size
        self.total += size.cost

    def showPizzaSummary(self):
        if len(self.ingredients)>0:
            print("\n\nUsted seleccionó una pizza {0} con: {1}"
            .format(self.size.name,','.join([ingredient.name for ingredient in self.ingredients])))
        else:
            print("\n\nUsted seleccionó una pizza margarita (básica) {0}"
            .format(self.size.name))
        print("{0} {1}: {2}".format(pizzaSubtotal,self.size.name,self.total))



class DividedPizza(Pizza):

    def __init__(self,zones):
        super(DividedPizza,self).__init__()
        self.divided = True
        self.zones = zones

    def addIngredient(self,ingredient,zone):
        if self.zones >= zone:
            if len(self.ingredients) < zone:
                self.ingredients.append([])
            self.ingredients[zone-1].append(ingredient)
            self.total += ingredient.cost/self.zones


    def deleteIngredient(self,ingredient,zone):
        if self.zones >= zone:
            self.ingredients[zone-1].remove(ingredient)
            self.total += ingredient.cost/self.zones


    def showPizzaSummary(self):
        print("\n\nUsted seleccionó una pizza dividida")
        for zone in self.ingredients:
            print("Zona {0}: {1}".format(self.ingredients.index(zone)+1,','.join([ingredient.name for ingredient in zone])))
        print("{0} {1} dividida: {2}".format(pizzaSubtotal,self.size.name,self.total))



class pizzaFactory:

    @staticmethod
    def getPizza(divided,zones=2): #mitad por defecto
        if divided:
            return DividedPizza(zones)
        elif not divided:
            return Pizza()
        else:
            return Pizza()
