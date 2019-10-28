'''
    modulo para inicializar los distintos tamaños e ingredientes por defecto
'''

from classes.characteristic import *


# lista con cada ingrediente (de tipo Ingredient)
baseIngredients = [
    Ingredient("Jamón",40,"ja"),
    Ingredient("Champiñones",35,"ch"),
    Ingredient("Pimentón",40,"pi"),
    Ingredient("Doble queso",40,"dq"),
    Ingredient("Aceitunas",58,"ac"),
    Ingredient("Pepperoni",38.5,"pp"),
    Ingredient("Salchichón",62.5,"sa")
]

# lista con cada tamano (de tipo Size)
baseSizes = [
    Size("Familiar",650,"f"),
    Size("Grande",580,"g"),
    Size("Mediana",430,"m"),
    Size("Pequeña",280,"p")
]
