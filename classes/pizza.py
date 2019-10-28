from .characteristic import Size
from util.cliMsg import *

class Pizza:
    '''
        Una clase pizza para crear tantas pizzas como
        el usuario requiera. Aqui se manejan los ingredientes
        seleccionados en una lista, el tamano seleccionado y
        cuanto costara la pizza después de haberle agregado
        tantos ingredientes como se requiera
    '''

    def __init__(self):
        '''
             la clase necesita una lista de ingredientes,
             un tamano y el total en precio. En este tipo
             de pizza por defecto no esta dividida y
             la cantidad de zonas es uno (2)
        '''
        self.ingredients = []
        self.size = None
        self.total = 0
        self.zones = 1
        self.divided = False


    def addIngredient(self,ingredient):
        '''
            Agregar un ingrediente a la pizza en cuestion

            Parametros:
               :param Ingredient ingredient: el objeto de tipo Ingredient que se agregara a la lista de ingredientes de la pizza

            :return: None
       '''
        self.ingredients.append(ingredient)
        self.total += ingredient.cost



    def deleteIngredient(self,ingredient):
        '''
            Eliminar un ingrediente de la pizza en cuestion

            Parametros:
               :param Ingredient ingredient: el objeto de tipo Ingredient que se eliminara de la lista de ingredientes de la pizza

            :return: None
       '''
        self.ingredients.remove(ingredient)
        self.total -= ingredient.cost


    def changeSize(self,size):
        '''
            cambiar el tamano de la pizza

            Parametros:
               :param Size size: el objeto de tipo Size que definira el tamano de la pizza

            :return: None
       '''
        self.size = size
        self.total += size.cost


    def showPizzaSummary(self):
        '''
            Metodo que permite mostrar un resumen de la pizza
            despues de personalizarla

            :return: None
       '''
        if len(self.ingredients)>0:
            print("\n\nUsted seleccionó una pizza {0} con: {1}"
            .format(self.size.name,','.join([ingredient.name for ingredient in self.ingredients])))
        else:
            print("\n\nUsted seleccionó una pizza margarita (básica) {0}"
            .format(self.size.name))
        print("{0} {1}: {2}".format(pizzaSubtotal,self.size.name,self.total))






class DividedPizza(Pizza):
    '''
          Una clase pizza Divida que extiende de pizza permite dividirla por zonas
          donde cada zona tiene ingredientes distintos. Esta clase
          mantiene la lista de ingredientes pero tiene sublistas
          por zona
    '''


    def __init__(self,zones):
        '''
             El atributo divided (dividida) se inicializa en verdadero
             y la cantidad de zonas es dinamica y se puede dividir en
             n zonas
        '''
        super(DividedPizza,self).__init__()
        self.divided = True
        self.zones = zones
        self._appendZones()


    def _appendZones(self):
        '''
             El atributo divided (dividida) se inicializa en verdadero
             y la cantidad de zonas es dinamica y se puede dividir en
             n zonas

             :return: None
        '''
        for i in range (0,self.zones):
            self.ingredients.append([])

    def addIngredient(self,ingredient,zone):
        if self.zones >= zone:
            self.ingredients[zone-1].append(ingredient)
            self.total += ingredient.cost/self.zones


    def deleteIngredient(self,ingredient,zone):
        if self.zones >= zone:
            self.ingredients[zone-1].remove(ingredient)
            self.total += ingredient.cost/self.zones


    def showPizzaSummary(self):
        print("\n\nUsted seleccionó una pizza dividida")
        for zone in range(0,len(self.ingredients)):
            if len(self.ingredients[zone])>0:
                print("Zona {0}: {1}".format(zone+1,','.join([ingredient.name for ingredient in self.ingredients[zone]])))
            else:
                print("Zona {0}: margarita".format(zone+1))
        print("{0} {1} dividida: {2}".format(pizzaSubtotal,self.size.name,self.total))





class pizzaFactory:

    @staticmethod
    def getPizza(divided,zones=2):
        '''
             permite obtener una pizza dividida o no
             dividia dependiendo del parametro que se le pase

             Parametros:
                :param bool divided: define si la pizza que va a instanciar y retornar es dividida o no
                :param int zones: define la cantidad de zonas en que se dividirá la pizza, por defecto es 2

            :return: Pizza
        '''
        if divided:
            return DividedPizza(zones)
        elif not divided:
            return Pizza()
        else:
            return Pizza()
