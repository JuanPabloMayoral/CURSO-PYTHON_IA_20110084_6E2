# Juan Pablo Mayoral L�pez 20110084 6E2
#Capitulo 27 - El bucle while en python
#Con el bucle while podr�s ejecutar una serie de declaraciones siempre que la condici�n se cumpla, que sea verdadera. Una vez se convierta en falsa, 
#va a dejar de ejecutar el c�digo del bucle.

 
 #Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
x = 0
print("ACTIVIDAD 1")
while x <= 15:
	print(x)
	x += 5

#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
x = 0
print("ACTIVIDAD 2")
while x >= -100:
	print(x)
	x -= 20

#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecuci�n esta frase con el valor de ejecuci�n correspondiente: 
#'El valor del bucle es 10'...
x = 10
print("ACTIVIDAD 3")
while x >= 0:
	print('El valor de x es: ', x)
	x -= 1
