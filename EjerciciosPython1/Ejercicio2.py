# 2. Clasificación de edad
# Pide al usuario su edad y muestra un mensaje:
#
# Menor de 18: “Eres menor de edad”.
# Entre 18 y 65: “Eres adulto”.
# Mayor de 65: “Eres mayor”.

edad = input("Dime tu edad: ")

edad = int(edad)




if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 65:
    print("Eres adulto")
else:
    print("Eres mayor")