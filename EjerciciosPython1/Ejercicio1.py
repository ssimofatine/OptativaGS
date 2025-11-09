### 1. Ejercicio
# 1. Conversión de temperaturas
# Escribe un programa que convierta grados Celsius a Fahrenheit.
# Fórmula: ( F = C x 9/5 + 32 ).

def convierta(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


numBoolean = True
while numBoolean:
    c1 = input("por favor Dime grado celsius: ")
    if convierta(c1):
        break
    else:
        print("tu numero no es numero entere porfa introduce comó este Ej(1, 2, 3, 55.4)")



c = float(c1)

F = (c * 9 / 5) + 32
print("--------------------")
print(f"{F} F")
print("Adios")