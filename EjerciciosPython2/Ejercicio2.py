###Ejercicio 2: Validador de contraseñas
#Escribe una función que valide si una contraseña cumple los siguientes criterios:

#Al menos 8 caracteres
#Al menos una letra mayúscula
#Al menos una letra minúscula
#Al menos un número
#Al menos un carácter especial (@, #, $, %, etc.)
#La función debe retornar True si cumple todos los criterios, False en caso contrario.


def mirar_password(la_clave):
    largo_bien = False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_raro = False

    if len(la_clave) >= 8:
        largo_bien = True

    cosas_raras = "@#$%&*"

    for letra in la_clave:
        if letra.isupper() == True:
            tiene_mayuscula = True
        if letra.islower() == True:
            tiene_minuscula = True
        if letra.isdigit() == True:
            tiene_numero = True
        if letra in cosas_raras:
            tiene_raro = True

    if largo_bien == True and tiene_mayuscula == True and tiene_minuscula == True and tiene_numero == True and tiene_raro == True:
        return True
    else:
        return False