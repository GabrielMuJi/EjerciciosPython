"""
Ejercicio 04

Escribir un programa que use un ciclo definido con rango numérico, que
averigüe a cuántos amigos quieren saludar, les pregunte los nombres de esos
amigos/as, y los salude.
"""

leyendo = True
while leyendo:
    numeroAmigos = input("Escribe tu número de amigos")
    try:
        numeroAmigos = int(numeroAmigos)
        leyendo = False
    except ValueError:
        print(numeroAmigos, "No es un número entero, pruebe de nuevo.")

for n in range(numeroAmigos):
    nombre = input("Escribe el nombre de tu amigo: ")
    print("Hola", nombre)
