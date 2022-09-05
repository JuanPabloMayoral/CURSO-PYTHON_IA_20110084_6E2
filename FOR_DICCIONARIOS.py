# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 32 - Como usar diccionarios con el bucle for en python
# Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:

print("ACTIVIDAD:")
teclado1 = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x in teclado1:
	print(x, '=', teclado1[x] + '.')