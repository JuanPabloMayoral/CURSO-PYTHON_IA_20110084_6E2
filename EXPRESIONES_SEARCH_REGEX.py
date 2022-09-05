#Juan Pablo Mayoral López 20110084 6E2
# Capitulo 47 - Expresiones regulares - search() - RegEx de python

import re
print("\nACTIVIDAD 1")
texto = "Bienvenido al programa"
busqueda = re.search("Bienvenidos", texto)
print(busqueda)

print("\nACTIVIDAD 2")
texto = "Bienvenido al programa"
busqueda = re.search("I", texto)
print(busqueda)

print("\nACTIVIDAD 3")
texto = "Bienvenido al programa"
busqueda = re.search("i", texto)
print(busqueda)