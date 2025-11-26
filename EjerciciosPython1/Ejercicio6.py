### 6. Máximo y mínimo de una lista

#Dada una lista de números (pedidos al usuario), muestra el número más pequeño y el más grande.

#---

lista_numeros = []
cantidad = int(input("cuantos numeros poner? "))

for i in range(cantidad):
    num = int(input("pon numero: "))
    lista_numeros.append(num)

numero_grande = lista_numeros[0]
numero_chico = lista_numeros[0]

for x in lista_numeros:
    if x > numero_grande:
        numero_grande = x
    if x < numero_chico:
        numero_chico = x

print("el mas grande es:", numero_grande)
print("el mas pequerno es:", numero_chico)