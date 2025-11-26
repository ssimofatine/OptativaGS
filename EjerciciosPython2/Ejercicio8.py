####Ejercicio 8: Diccionario de longitudes
##Dada una lista de strings, crea un diccionario usando comprehension donde las claves sean las palabras y los valores su longitud.

##Ejemplo:

##palabras = ["Python", "Java", "JavaScript", "C++"]
#### {'Python': 6, 'Java': 4, 'JavaScript': 10, 'C++': 3}




lista_cosas = ["Python", "Java", "JavaScript", "C++"]
diccionario_largo = {cosa: len(cosa) for cosa in lista_cosas}
print(diccionario_largo)