# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 33 - Metodos con diccionarios en python
#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. 
#Muestra la última clave ('Modelo') que queda en la consola.

print("ACTIVIDAD:")

teclado1 = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}


teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1

del teclado2['Categoria']

del teclado2['Precio']

print(teclado2['Modelo'])
