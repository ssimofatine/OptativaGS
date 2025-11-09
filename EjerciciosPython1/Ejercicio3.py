# 3. Números pares en un rango
# Solicita dos números enteros y muestra todos los pares que se encuentran en ese intervalo.

def ValorDosNumero1(numero1):
    try:

        int(numero1)
        return True
    except ValueError:
        print(f"Error:[{numero1}] no correcto")
        return False

def ValorDosNumero2(numero2):
    try:

        int(numero2)
        return True
    except ValueError:
        print(f"Error:[{numero2}] no correcto")
        return False

numBoolean = True

while numBoolean:
    numero1 = input("Introduce numero uno: ")
    numero2 = input("Introduce numero dos: ")
    if ValorDosNumero1(numero1) and ValorDosNumero2(numero2):
        numero1 = int(numero1)
        numero2 = int(numero2)
        numBoolean = False
    else:
        print("porfa introduce dos numeros enteros como este Ej(1, 2, 3, 4, 44, ....)")



# este metodo usa min() y max() para coge numero mayor or menor
n1 = min(numero1, numero2)
n2 = max(numero1, numero2)

print(f" tu tienes dos numeros Pares es:  [{n1}, {n2}]:")


for i in range(n1, n2 + 1):
    if i % 2 == 0:
        print(i)

