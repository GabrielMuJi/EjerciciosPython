"""
Ejercicio 02

Usando las funciones del ejercicio anterior, escribir un programa que lea de
teclado dos tiempos expresados en horas, minutos y segundos; las sume y
muestre el resultado en horas, minutos y segundos por pantalla.
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
        horas1 = int(input("Introduce el número de horas de la primera hora."))
        minutos1 = int(input("Introduce el número de minutos de la primera hora."))
        segundos1 = int(input("Introduce el número de segundos de la primera hora."))
        horas2 = int(input("Introduce el número de horas de la segunda hora."))
        minutos2 = int(input("Introduce el número de minutos de la segunda hora."))
        segundos2 = int(input("Introduce el número de segundos de la segunda hora."))
        leyendo = False
    except ValueError:
        print("No ha introducido valores numéricos")

print("La primera hora es: ",horas1,minutos1,segundos1)
print("La segunda hora es: ",horas2,minutos2,segundos2)
hora1segundos = pasarASegundos(horas1,minutos1,segundos1)
hora2segundos = pasarASegundos(horas2,minutos2,segundos2)
segundosTotales = hora1segundos+hora2segundos
print("La suma de ambas horas asciende a: ", pasarAHms(segundosTotales))