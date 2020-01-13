"""
Ejercicio 06

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
"""

def convertirACelsius (tempF):
    return (tempF - 32) * 5/9

leyendo = True
while leyendo:
    try:
        fahrenheit = float(input("Introduzca la temperatura en grados Fahrenheit: "))
        leyendo = False
    except ValueError:
        print ("No ha introducido un valor correcto.")
celsius = convertirACelsius(fahrenheit)
print(fahrenheit," F son ", celsius, " ºC")