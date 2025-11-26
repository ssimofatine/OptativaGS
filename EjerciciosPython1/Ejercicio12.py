### 12. Número primo

#Escribe un programa que determine si un número ingresado por el usuario es primo o no.

#---


numero_ver = int(input("pon numero para ver si primo: "))
es_primo_verdad = True

if numero_ver < 2:
    es_primo_verdad = False
else:
    for i in range(2, numero_ver):
        if numero_ver % i == 0:
            es_primo_verdad = False

if es_primo_verdad == True:
    print("si es primo")
else:
    print("no es primo")