#Juan Pablo Mayoral López 20110084 6E2
# Capitulo 49 - Expresiones regulares - split() y sub() en python

import re
#se separa las palabras espcaio por espacio en un string
print("\nACTIVIDAD 1")
texto = "Pepe pena pica pina pica pina pepe pena"
busqueda = re.split(" ", texto)
print(busqueda)

# Esta forma es para ecluir y dividir las letras que se le pida
print("\nACTIVIDAD 2")
texto = "Pepe pena pica pina pica pina pepe pena"
busqueda = re.split("na", texto)
print(busqueda)

# Es divir el 4 argumento del texto que tenemos sin separarlo
print("\nACTIVIDAD 3")
texto = "Pepe pena pica pina pica pina pepe pena"
busqueda = re.split(" ", texto, 4)
print(busqueda)

# En el primer argumento se especifica lo que quieres buscar, en el segundo lo que quieres que se reemplace en las coincidencias y el tercero es de donde quieres hacer estas acciones.
print("\nACTIVIDAD 4")
texto = "Pepe pena pica pina pica pina pepe pena"
busqueda = re.sub(" ",  "-",  texto)
print(busqueda)

#  limitar los resultados que reemplaza sub() añadiendo el número como cuarto parámetro:
print("\nACTIVIDAD 5")
texto = "Pepe pena pica pina pica pina pepe pena"
busqueda = re.sub(" ",  "-",  texto, 4)
print(busqueda)