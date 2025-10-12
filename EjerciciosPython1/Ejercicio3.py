# 3. Números pares en un rango
# Solicita dos números enteros y muestra todos los pares que se encuentran en ese intervalo.

try:

    numero1 = input("Introduce numero uno: ")

    numero1 = int(numero1)

    numero2 = input("Introduce numero dos: ")

    numero2 = int(numero2)

    # este metodo usa min() y max() para coge numero mayor or menor
    n1 = min(numero1, numero2)
    n2 = max(numero1, numero2)

    print(f" tu tienes dos numeros Pares es:  [{n1}, {n2}]:")


    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            print(i)

except ValueError:
    print("Error: no correcto")