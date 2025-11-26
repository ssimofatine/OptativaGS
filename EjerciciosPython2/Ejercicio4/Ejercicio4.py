###Módulos
#Ejercicio 4: Utilidades de strings
#Crea un módulo string_utils.py con las siguientes funciones:

#invertir_texto(texto): Invierte el orden de los caracteres
#contar_vocales(texto): Cuenta cuántas vocales hay
#es_palindromo(texto): Verifica si es un palíndromo
#capitalizar_palabras(texto): Capitaliza la primera letra de cada palabra
#Importa y usa estas funciones en otro archivo.




def invertir_texto(texto):
    return texto[::-1]

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    cuenta = 0
    for letra in texto:
        if letra in vocales:
            cuenta = cuenta + 1
    return cuenta

def es_palindromo(texto):
    reves = texto[::-1]
    if texto == reves:
        return True
    else:
        return False

def capitalizar_palabras(texto):
    return texto.title()