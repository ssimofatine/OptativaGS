###Ejercicio 1: Calculadora de estadísticas
#Crea una función que reciba una lista de números y retorne un diccionario con la media, mediana y moda.

#Ejemplo:

#numeros = [1, 2, 2, 3, 4, 5, 5, 5, 6]
#resultado = calcular_estadisticas(numeros)
# {'media': 3.67, 'mediana': 4, 'moda': 5}

def sacar_cuentas(lista_numeros):
    # media
    suma_total = 0
    cantidad = 0
    for x in lista_numeros:
        suma_total = suma_total + x
        cantidad = cantidad + 1
    la_media = suma_total / cantidad

    # mediana
    lista_numeros.sort()
    mitad = int(cantidad / 2)
    if cantidad % 2 == 0:
        la_mediana = (lista_numeros[mitad - 1] + lista_numeros[mitad]) / 2
    else:
        la_mediana = lista_numeros[mitad]

    # moda
    cuenta_maxima = 0
    numero_moda = lista_numeros[0]
    for i in lista_numeros:
        cuantas_veces = lista_numeros.count(i)
        if cuantas_veces > cuenta_maxima:
            cuenta_maxima = cuantas_veces
            numero_moda = i

    diccionario_final = {}
    diccionario_final['media'] = la_media
    diccionario_final['mediana'] = la_mediana
    diccionario_final['moda'] = numero_moda

    return diccionario_final