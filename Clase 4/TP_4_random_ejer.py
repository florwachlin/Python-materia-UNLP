#Ejercicio sugerido

#Crea una lista con tus comidas o películas favoritas y hace que Python elija una al azar.

import random

comidas_favoritas= ["tacos", "pollo con fideos", "sandwiches"]
random_comida= random.choice(comidas_favoritas)
print(random_comida)