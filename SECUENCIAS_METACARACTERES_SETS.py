#Juan Pablo Mayoral L�pez 20110084 6E2
# Capitulo 50 - Secuencias especiales, metacaracteres y sets

import re
#Buscar� en el string si hay los caracteres comprendidos entre el rango de letras de la e a la q.
texto = "\nBienvenidos a mi programa de secuencias en python"
buscar = re.findall("[c-j]", texto)
print(buscar)


texto = "\nVan al zoologico?"
buscar = re.findall("zo{2}logico", texto)
if buscar:
	print("\nSe encontro una similitud.")
else:
	print("\nNo hay similitudes.")




texto = "\nEl futuro es ahora."
buscar = re.findall("ayer|ahora", texto)
if buscar:
	print("\nSe encontro una similitud.")
else:
	print("\nNo hay similitudes.")



texto = "\nLa programacion en python es mas facil que en c++."
buscar = re.findall("progra..cion", texto)
if buscar:
	print("\nSe encontro una similitud.")
else:
	print("\nNo hay similitudes.")

#Buscar� cualquier car�cter excepto e, l.
texto = "Se acerca el invierno."
buscar = re.findall("^el", texto)
if buscar:
	print("\nHay al menos una coincidencia.")
else:
	print("\nNo hay coincidencias.")




#si pones en el set el s�mbolo d�lar, buscar� ese s�mbolo literalmente en un string.
texto = "Se acerca el invierno."
buscar = re.findall("invierno.$", texto)
if buscar:
	print("\nHay al menos una coincidencia.")
else:
	print("\nNo hay coincidencias.")