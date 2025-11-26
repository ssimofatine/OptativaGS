numero_persona = int(input("dame numero positivo: "))
resultado_total = 1

for i in range(1, numero_persona + 1):
    resultado_total = resultado_total * i

print("el factorial es:", resultado_total)