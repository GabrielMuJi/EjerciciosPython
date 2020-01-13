"""
Ejercicio 05

Escribir un programa que le pregunte al usuario una cantidad de euros, una
tasa de interés y un número de años y muestre como resultado el monto final a
obtener. La fórmula a utilizar es (interés compuesto):

Cf = Ci * (1 + i/100) ^ n

Donde Ci es el capital inicial, i es la tasa de interés y n es el número de
años a calcular.
"""

def interesCompuesto(capitalInicial,interes,anios):
    return capitalInicial * (1 + interes/100) ** anios

leyendo = True
while leyendo:
    try:
        ci = float(input("Introduce el capital inicial: "))
        anios = float(input("Introduce los años: "))
        interes = float(input("Introduce el interes (%): "))
        leyendo = False
    except ValueError:
        print("Hay un fallo en la introducción de datos")
print ("El total a pagar es de: ", interesCompuesto(ci, interes, anios), " euros")

