# Juan Pablo Mayoral L�pez 20110084 6E2
#Capitulo 23 - El condicional IF ELIF ELSE INPUT

#Al siguiente c�digo a�adirle un par de rangos de edad. Uno de 18 a�os hasta 45 y otro de m�s de 100 a�os hasta 120.
#edad = int(input('�Cu�l es tu edad?\n'))
#if edad <= 0:
#	print('Nadie puede tener esa edad.')
#elif edad <= 1 and edad < 18:
#	print('Eres menor de edad.')
#elif edad <= 100:
#	print('Eres mayor de edad.')
#else:
#	print('Edad no v�lida.')
edad=int(input("Cual es tu edad?\n"))
if edad <= 0:
	print('Me crees tonto.')
elif edad <= 1 and edad < 18:
	print('Eres todavia chico.')
elif edad == 18 and edad <= 45:
	print('Eres ya todo un hombre.')
elif edad <= 100:
	print('Eres mayor de edad.')
elif edad > 100 and edad <= 120:
	print('Eres viejo.')
else:
	print('No se puede esa edad.')
