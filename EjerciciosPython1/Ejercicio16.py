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