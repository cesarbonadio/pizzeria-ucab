class Characteristic:
    def __init__(self,name,cost,abbr):
        self.name = name
        self.cost = cost
        self.abbr = abbr

class Ingredient(Characteristic):
    pass

class Size(Characteristic):
    pass
