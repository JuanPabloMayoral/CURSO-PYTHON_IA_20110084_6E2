# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 44 - Importar modulos y las funciones lambda en python
import math

#En esta parte se define la variable area y se imprta la libreria math para poder hacer calculos
#con la palabra round() podemos acortar los decimales que queremos del resultado
print("ACTIVIDAD 1")
def area(radio):
    resultado = round(math.pi * radio * radio, 3)
    print(resultado)

area(2)
#Aqui se simplifica a una linea todo el programa de arriba con lambda
print("ACTIVIDAD 2")

area = lambda radio: round(math.pi * radio * radio, 3)

print(area(2))
