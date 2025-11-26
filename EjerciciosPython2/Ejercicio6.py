###List Comprehension
#Ejercicio 6: Números al cuadrado
#Genera una lista con los cuadrados de los números pares del 1 al 50 usando list comprehension.

#Resultado esperado:

#[4, 16, 36, 64, ..., 2500]


numeros_pares = [x**2 for x in range(1, 51) if x % 2 == 0]
print(numeros_pares)