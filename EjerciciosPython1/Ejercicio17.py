lista_a = [2, 3, 4]
lista_b = [5, 1, 2]
resultado_escalar = 0

# longitud es 3
for i in range(3):
    multi = lista_a[i] * lista_b[i]
    resultado_escalar = resultado_escalar + multi

print("producto escalar es:", resultado_escalar)