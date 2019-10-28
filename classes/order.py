from .pizza import Pizza

class Order:
    '''
        Una clase orden para manetener todas las pizzas
        seleccionadas en una ejecución en un solo lugar
   '''

    def __init__(self):
        '''
            La clase Order tiene una lista de pizzas

            :return: None
        '''
        self.pizzas = []


    def addPizza(self,pizza):
        '''
            agregar una pizza a la orden

            :return: None
       '''
        self.pizzas.append(pizza)


    def showOrderSummary(self):
        '''
            Mostrar un resumen de cuantas pizzas se pidieron
            y el total a pagar al finalizar la orden

            :return: None
        '''
        print("\nEl pedido tiene un total de {0} pizza(s) por un monto de {1}"
        .format(len(self.pizzas),sum([pizza.total for pizza in self.pizzas])))
        print("\nGracias por su compra, regrese pronto")
