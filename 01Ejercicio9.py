"""
Ejercicio 06

Escribir un programa que reciba un número n por parámetro e imprima los
primeros números triangulares, junto con su índice.
Los números triangulares se obtienen mediante la suma de los números naturales
desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el
programa debe imprimir:

1 - 1
2 - 3
3 - 6
4 - 10
5 - 15

Nota: hacerlo usando y sin usar la ecuación n * (n + 1) / 2. ¿Cuál realiza más
operaciones? (Respuesta: triangularIterativo con diferencia)
"""

def triangularIterativo(numero):
    resultado = 0
    for i in range (1,numero+1,1):
        resultado = resultado + i
    return resultado

def triangularEcuacion(numero):
    resultado = numero * (numero+1) / 2
    return resultado

leyendo = True
while leyendo:
    try:
        numero = int(input("Introduzca un número entero: "))
        leyendo = False
    except ValueError:
        print ("No has introducido un número entero")
print("De manera matemática: ", triangularEcuacion(numero))
print("De manera iterativa: ", triangularIterativo(numero))