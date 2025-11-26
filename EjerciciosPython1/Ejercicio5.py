### 5. Lista invertida

##Crea una lista con 5 números introducidos por el usuario y luego muéstrala invertida.



lista_caja = []

numero_uno = input("pon numero 1: ")
lista_caja.append(numero_uno)

numero_dos = input("pon numero 2: ")
lista_caja.append(numero_dos)

numero_tres = input("pon numero 3: ")
lista_caja.append(numero_tres)

numero_cuatro = input("pon numero 4: ")
lista_caja.append(numero_cuatro)

numero_cinco = input("pon numero 5: ")
lista_caja.append(numero_cinco)

lista_otra = []

lista_otra.append(lista_caja[4])
lista_otra.append(lista_caja[3])
lista_otra.append(lista_caja[2])
lista_otra.append(lista_caja[1])
lista_otra.append(lista_caja[0])

print(lista_otra)