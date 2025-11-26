####Manejo de Excepciones
##Ejercicio 12: División segura
###Crea una función division_segura(a, b) que divida dos números y maneje las siguientes excepciones:

##ZeroDivisionError: Si se intenta dividir por cero
#ValueError: Si los valores no son numéricos
#TypeError: Si los tipos de datos son incorrectos
#La función debe retornar el resultado o un mensaje de error apropiado.





def division_segura(numero_uno, numero_dos):
    try:
        resultado = numero_uno / numero_dos
        return resultado
    except ZeroDivisionError:
        return "error no dividir por cero"
    except ValueError:
        return "error deben ser numeros"
    except TypeError:
        return "error tipo dato malo"