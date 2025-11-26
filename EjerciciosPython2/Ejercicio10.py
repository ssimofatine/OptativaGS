###Ejercicio 10: Filtrar números
#Usa filter() con lambda para obtener solo los números que sean divisibles por 3 Y por 5 (es decir, divisibles por 15) de una lista.

#Ejemplo:

#numeros = [15, 30, 7, 45, 60, 12, 90]
##3 Resultado: [15, 30, 45, 60, 90]


numeros_lista = [15, 30, 7, 45, 60, 12, 90]
solo_quince = list(filter(lambda n: n % 3 == 0 and n % 5 == 0, numeros_lista))
print(solo_quince)