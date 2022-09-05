# Juan Pablo Mayoral López 20110084 6E2
#Capitulo 24 - Comprobar datos en listas y tuplas en python

print("ACTIVIDAD")
#Se va hacer una tupla con colores ya establecidos y mediante las condicionales 
#se le dira al usuario que ingrese un color y si este no esta en la tupla se le hara saber

colores = input('Introduce un color:\n')
tupla_colores = ('morado', 'naranja', 'rojo', 'rosa')
if colores in tupla_colores[0]:
	print('El color morado esta admitido')
elif colores in tupla_colores[1]:
	print('El color naranja esta admitido')
elif colores in tupla_colores[2]:
	print('El color rojo esta admitido')
elif colores in tupla_colores[3]:
	print('El color rosa esta admitido')
else:
	print('Color no admitido')