###Ejercicio 5: Gestor de fechas
#Usa el módulo datetime para crear una función que:

#Reciba una fecha de cumpleaños (día, mes, año)
#Calcule cuántos días faltan para el próximo cumpleaños
#Si ya pasó este año, calcule para el próximo año


import datetime


def ver_cumple(dia, mes, anio):
    hoy = datetime.date.today()
    fecha_nacimiento = datetime.date(anio, mes, dia)
    cumple_este_anio = datetime.date(hoy.year, mes, dia)

    if cumple_este_anio < hoy:
        cumple_proximo = datetime.date(hoy.year + 1, mes, dia)
        dias_faltan = cumple_proximo - hoy
        return dias_faltan.days
    else:
        dias_faltan = cumple_este_anio - hoy
        return dias_faltan.days