frase_escrita = input("escribe algo aqui: ")
caja_conteo = {}

for letra in frase_escrita:
    if letra in caja_conteo:
        caja_conteo[letra] = caja_conteo[letra] + 1
    else:
        caja_conteo[letra] = 1

print(caja_conteo)