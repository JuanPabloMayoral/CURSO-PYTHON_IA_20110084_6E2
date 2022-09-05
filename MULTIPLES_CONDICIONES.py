# Juan Pablo Mayoral López 20110084 6E2
#Capitulo 25 - Multiples condiciones IF en python

print("ACTIVIDAD")
print("Saludos amigo que deseas comprar?\n" + "Comida disponible:\n" +
      "1- Hamburguesas: 80 pesos.\n" + 
      "2- Pizza: 50 pesos.\n" + 
      "3- Helado: 15 pesos.\n" +
      "4- Alitas: 75 pesos.\n")
#Aqui en los corchetes el usuario debe escoger su comida y se ira agregando lo que pida
comprar = [0]
dinero = 200
hamburguesa = 80
pizza = 50
helado = 15
alitas= 75

if 0 in comprar or comprar == []:
    print("Escoge una de las opciones del 1 al 4.")

if 1 in comprar:
    dinero = dinero - hamburguesa

if 2 in comprar:
    dinero = dinero - pizza

if 3 in comprar:
    dinero = dinero - helado

if 4 in comprar:
    dinero = dinero - alitas

else:
    print("Solo puedes escoger del 1 al 4.")

if dinero < 0:
    print("No tienes el dinero sufuciente bro")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print("Te quedan "+ str(dinero) + "pesos")
    print("Se agrego la comida a tu cuenta.")

