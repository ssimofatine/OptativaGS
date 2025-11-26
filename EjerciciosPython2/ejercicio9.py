###Funciones Lambda
#Ejercicio 9: Ordenar por criterio
#Usa una función lambda con sorted() para ordenar una lista de tuplas (nombre, edad, altura) por edad de menor a mayor.

#Ejemplo:

#personas = [("Ana", 25, 165), ("Juan", 30, 175), ("María", 22, 160)]
### Resultado: [("María", 22, 160), ("Ana", 25, 165), ("Juan", 30, 175)]



gente = [("Ana", 25, 165), ("Juan", 30, 175), ("Maria", 22, 160)]
gente_ordenada = sorted(gente, key=lambda persona: persona[1])
print(gente_ordenada)