### 8. Tabla de multiplicar

#Solicita un número y genera su tabla de multiplicar del 1 al 10.

#---

numero_tabla = int(input("que numero tabla quieres? "))

for i in range(1, 11):
    valor = numero_tabla * i
    print(numero_tabla, "por", i, "es", valor)