"""
Ejercicio 10

Escribir un programa que tome una cantidad "m" de valores ingresados por el
usuario, a cada uno le calcule el factorial e imprima el resultado junto con
el número de orden correspondiente.
"""

def calcularFactorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado = resultado * i
    return resultado

leyendo = True
while leyendo:
    try:
        numeroOrdenes = int(input("Introduce el número de numeros de los cuales desea obtener el factorial"))
        leyendo = False
    except ValueError:
        print("No has introducido un valor numérico")

for i in range (1, numeroOrdenes+1):
    leyendo = True
    while leyendo:
        try:
            numero = int(input("Introduce el número del cual desea obtener el factorial: "))
            leyendo = False
        except ValueError:
            print("No has introducido un valor numérico")
    print("Esta es la orden número: ",i)
    print("El factorial de esta orden (",numero,") corresponde a: ",calcularFactorial(numero))
    print("====================================================================")