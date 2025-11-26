### 16. Lista ordenada

#Pide al usuario ingresar varios números, guárdalos en una lista y muestra:

#- La lista original.
#- La lista ordenada ascendentemente.
#- La lista ordenada descendentemente.

##---


lista_numeros = []
cuantos = int(input("cuantos numeros?: "))

for i in range(cuantos):
    n = int(input("pon numero: "))
    lista_numeros.append(n)

print("original:", lista_numeros)

lista_numeros.sort()
print("arriba:", lista_numeros)

lista_numeros.sort(reverse=True)
print("abajo:", lista_numeros)