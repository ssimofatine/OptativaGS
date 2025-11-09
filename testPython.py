# for con range
for i in range(5):
    print(i)

print("----------------")

for i in range(1, (20+1)):
    print(i)

print("----------------")
language = 'Python'
for letter in language:
    print(letter)

print("----------------")

print(len(language))
print("-----------------")

for i in range(len(language)):
    print(f"--- {i} ---")
    print(language[i])

print("----------------")
contador = 7
if contador > 4 and contador < 11:
    print(f"--------   {contador}   --------")


print("---------------")

for i in range(-1,(-6 -1),-1):
    print(i)

print("----------------------")

for i in range(10, 0, -1):
    print(i)

print("-----------------------")

for i in range(100, -1, -10):
    print(i)

print("------------------------")
conjunto = {1, 2, 3, 4, 5}
for num in conjunto:
    print(num)

print("------------------------")

numeroUno = {1, 2, 3, 4, 5}

for simoH in numeroUno:
    print(simoH)

print("--------------------------")

# for sobre diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
for clave in persona:
    print(clave, persona[clave])

print("-----------------------")
for clave, valor in persona.items():
    print(clave, valor)
else:
    print("Bucle terminado")


print("--------------")

simohaji = {"simo", "haji", "kamal", "morad"}

##hajisimo = simohaji.index("kamal")


