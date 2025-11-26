###Ejercicio 7: Filtrar palabras
#Dada una lista de palabras, crea una nueva lista solo con las palabras que tengan más de 5 letras usando list comprehension.

#Ejemplo:

###palabras = ["sol", "python", "casa", "programación", "gato", "computadora"]
# ####Resultado: ['python', 'programación', 'computadora']



palabras = ["sol", "python", "casa", "programacion", "gato", "computadora"]
palabras_largas = [p for p in palabras if len(p) > 5]
print(palabras_largas)