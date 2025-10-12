# Contador de vocales
# Pide al usuario una palabra y muestra cuántas vocales contiene.

# aqui pide al usuario una palabra
balabra = input("dime tú palabra: ")

# aqui almacinar total del vocales
contador = 0

# aqui escribe todo letras del vocales
laletra = "aieouAIEOUáíéóúÁÉÍÓÚ"

# ahora mejor usa metodo de ( FOR con IF )

for i in balabra:
    if i in laletra:
        contador = contador + 1

print(f"La palabra '{balabra}' tiene {contador} vocales.")




