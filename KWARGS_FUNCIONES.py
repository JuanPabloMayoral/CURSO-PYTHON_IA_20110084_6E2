# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 36 - KWARGS DICCIONARIOS ARBITRARIOS EN PYTHON

from tkinter import Y


print("ACTIVIDAD")
def colores (**kwargs):
    print("Este es el color " + kwargs["color1"] + ".")

colores(color1="rojo", color2="azul", color3="verde", color4="amarillo")

print("\nACTIVIDAD 2")
def suma (x,y):
    return x+y
total = suma (10,10)
print(total)

def resta (x,y):
    return x-y
total = suma (10,10)
print(total)

def multi (x,y):
    return x*y
total = multi (10,10)
print(total)


def division (x,y):
    return x/y
total = division (10,10)
print(total)

print("\nACTIVIDAD 3")
def colores(color="morado"):
    print("Mi color favorito es el:" + color)

colores("azul")
colores()
colores("verde")

