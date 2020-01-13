"""
Ejercicio 07
Utilice el programa anterior para generar una tabla de conversión de
temperaturas, desde 0º F hasta 120º F, de 10 en 10.
"""
def convertirACelsius(tempF):
    return (tempF - 32)*5/9


print("Grados Fahrenheit     Grados Celsius")
print("===============================================")
for tempF in range(0, 121, 10):
    print("      ", tempF, "         ", convertirACelsius(tempF))
