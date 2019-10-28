class Characteristic:
    '''
        Caracteristicas que puedan tener la pizza
        cada caracteristica tomada en cuenta en el proyecto
        tiene algo en comun: nombre, costo y una abreviatura
        para identificar la seleccion por terminal
   '''
    def __init__(self,name,cost,abbr):
        self.name = name
        self.cost = cost
        self.abbr = abbr

class Ingredient(Characteristic):
    pass

class Size(Characteristic):
    pass
