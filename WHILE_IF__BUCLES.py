# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 28 - Agregar if dentro de bucles while

#EL VALOR INICIAL DE LA X DEBE DE SER 0
x = 0
print("ACTIVIDAD")
# WHILE SE DEBE EJECUTAR MENOR IGUAL AL 30
while x <= 30:
	x += 1  

#IF PARA IR SALTANDO EN EL BUCLE
	if x == 4 or x == 6 or x == 10:
		print('Se salto el valor ', x, ' de x')
		continue

	#ESTE IF ES PARA ROMPER LA EJECUCION DE BUCLE
	if x == 15:
		print('Se rompio la ejecucion del bucle cuando x valia: ', x)
		break

	print(x)
