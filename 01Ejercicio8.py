"""
Ejercicio 08

Escribir un programa que imprima todos los números pares entre dos números que
se le pidan al usuario
"""

leyendo = True
while leyendo:
    try:
        numero1 = int(input("Introduzca el 1er número "))
        numero2 = int(input("Introduzca el 2do número "))
        leyendo = False
    except ValueError:
        print("Introduzca valores numéricos")

numero1 += numero1 % 2
for i in range(numero1,numero2,2):
    print(i)