### 15. Diccionario de frecuencias de palabras

#Dada una frase ingresada por el usuario, construye un diccionario en el que las claves sean palabras y los valores el número de veces que aparece cada una.

#--


frase_larga = input("pon una frase: ")
lista_palabras = frase_larga.split()
diccionario_cuentas = {}

for palabra in lista_palabras:
    if palabra in diccionario_cuentas:
        diccionario_cuentas[palabra] = diccionario_cuentas[palabra] + 1
    else:
        diccionario_cuentas[palabra] = 1

print(diccionario_cuentas)