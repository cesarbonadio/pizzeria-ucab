from .pizza import Pizza

class Order:

    def __init__(self):
        self.pizzas = []

    def addPizza(self,pizza):
        self.pizzas.append(pizza)

    def showOrderSummary(self):
        print("\nEl pedido tiene un total de {0} pizza(s) por un monto de {1}"
        .format(len(self.pizzas),sum([pizza.total for pizza in self.pizzas])))
        print("\nGracias por su compra, regrese pronto")
