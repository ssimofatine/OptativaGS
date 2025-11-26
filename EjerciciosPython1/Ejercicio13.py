### 13. Suma de elementos de una matriz

#Crea una matriz (lista de listas) de 2x3 con valores introducidos por el usuario y calcula la suma de todos sus elementos.

#---

matriz_caja = []
# fila 1
fila_uno = []
n1 = int(input("fila 1 num 1: "))
fila_uno.append(n1)
n2 = int(input("fila 1 num 2: "))
fila_uno.append(n2)
n3 = int(input("fila 1 num 3: "))
fila_uno.append(n3)
matriz_caja.append(fila_uno)

# fila 2
fila_dos = []
n4 = int(input("fila 2 num 1: "))
fila_dos.append(n4)
n5 = int(input("fila 2 num 2: "))
fila_dos.append(n5)
n6 = int(input("fila 2 num 3: "))
fila_dos.append(n6)
matriz_caja.append(fila_dos)

suma_todo = 0

for fila in matriz_caja:
    for numero in fila:
        suma_todo = suma_todo + numero

print("suma total matriz:", suma_todo)