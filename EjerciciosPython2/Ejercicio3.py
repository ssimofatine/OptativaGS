###Ejercicio 3: Contador de palabras
##Crea una función que reciba un texto y retorne un diccionario con la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y signos de puntuación).

#Ejemplo:

#texto = "Python es genial. Python es poderoso y Python es versátil."
#contar_palabras(texto)
# {'python': 3, 'es': 3, 'genial': 1, 'poderoso': 1, 'y': 1, 'versátil': 1}
def contar_cosas(texto_grande):
    texto_limpio = texto_grande.replace(".", "").replace(",", "")
    texto_chico = texto_limpio.lower()
    lista_palabras = texto_chico.split()

    diccionario_cuentas = {}

    for palabra in lista_palabras:
        if palabra in diccionario_cuentas:
            diccionario_cuentas[palabra] = diccionario_cuentas[palabra] + 1
        else:
            diccionario_cuentas[palabra] = 1

    return diccionario_cuentas