### 9. Diccionario de estudiantes

#Crea un diccionario donde la clave sea el nombre de un estudiante y el valor su nota. Después:

#- Añade 3 estudiantes.
#- Muestra el promedio de las notas.

#---



libro_notas = {}

nombre1 = input("nombre estudiante 1: ")
nota1 = float(input("nota estudiante 1: "))
libro_notas[nombre1] = nota1

nombre2 = input("nombre estudiante 2: ")
nota2 = float(input("nota estudiante 2: "))
libro_notas[nombre2] = nota2

nombre3 = input("nombre estudiante 3: ")
nota3 = float(input("nota estudiante 3: "))
libro_notas[nombre3] = nota3

suma_notas = 0
cantidad_gente = 0

for clave in libro_notas:
    suma_notas = suma_notas + libro_notas[clave]
    cantidad_gente = cantidad_gente + 1

media_final = suma_notas / cantidad_gente
print("la media es:", media_final)