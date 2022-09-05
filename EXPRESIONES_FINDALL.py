#Juan Pablo Mayoral López 20110084 6E2
# Capitulo 48 - Expresiones regulares - findall() - RegEx en python


import re

print("ACTIVIDA 1")
texto = "Pepe pena pica pina pica pina pepe pena"

busqueda = re.findall("e",texto)

print(busqueda)


print("ACTIVIDA 2")
texto = "Pepe pena pica pina pica pina pepe pena"
busqueda = re.findall("pe", texto)
print(busqueda)

