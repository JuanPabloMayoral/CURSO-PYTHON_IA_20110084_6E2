# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 35 - Como utilizar args en las funciones

print("ACTIVIDAD 1 :")
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marron', 'naranja')

def colores(*args):
	print('El color', args[0], 'es mi favorito.', 'El color', args[1], 'tampoco esta mal.')

colores('morado', 'azul')

print("ACTIVIDAD 2 :")
def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco numeros 8, 10, 52, 7623, 1, 9 es:\n', resultado)

suma(8, 10, 52, 7623, 1, 9)


