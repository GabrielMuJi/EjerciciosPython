"""
Ejercicio 01

Escribir dos funciones que permitan calcular:
    La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
"""

def pasarASegundos(horas,minutos,segundos):
    return ((horas*60)+minutos)*60+segundos

def pasarAHms(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    return (horas,minutos,segundos)

leyendo = True
while leyendo:
    try:
        numero1 = int(input("Introduce el número de horas."))
        numero2 = int(input("Introduce el número de minutos."))
        numero3 = int(input("Introduce el número de segundos."))
        print("===================================")
        numero4 = int(input("Introduce un número de segundos."))
        leyendo = False
    except ValueError:
        print("No ha introducido un valor numérico.")

print("La primera operación da un resultado de: ",pasarASegundos(numero1, numero2, numero3)," segundos")
print("La segunda operación da un resultado de: ",pasarAHms(numero4)," hms")

