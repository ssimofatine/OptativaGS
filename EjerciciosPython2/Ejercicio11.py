###Ejercicio 11: Mapeo de temperaturas
#Convierte una lista de temperaturas en Celsius a Fahrenheit usando map() y lambda. La fórmula es: F = (C × 9/5) + 32

#Ejemplo:

#celsius = [0, 10, 20, 30, 40]
### Resultado: [32.0, 50.0, 68.0, 86.0, 104.0]



grados_c = [0, 10, 20, 30, 40]
grados_f = list(map(lambda c: (c * 9/5) + 32, grados_c))
print(grados_f)
