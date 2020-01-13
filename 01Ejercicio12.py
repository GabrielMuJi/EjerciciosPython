"""
Ejercicio 12
Modificar el programa anterior para que pueda generar fichas de un juego que
puede tener números de 0 a n.
"""

leyendo = True
while leyendo:
    try:
        numeroMaximo = int(input("Introduce el número máximo que se mostrará en las fichas: "))
        leyendo = False
    except ValueError:
        print("No ha introducido un valor numérico")
for i in range(numeroMaximo+1):
    print("Fichas ",i)
    for j in range(i,numeroMaximo+1):
        print(i,j)
    print("=====")