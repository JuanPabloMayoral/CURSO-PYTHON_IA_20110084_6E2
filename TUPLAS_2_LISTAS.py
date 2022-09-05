# Juan Pablo Mayoral López 20110084 6E2
#Capitulo 20 - Como convertir una lista en una tupla y viceversa en python
#Convertir la siguiente lista en una tupla y asegúrate que se haya convertido en tupla correctamente imprimiendo en la consola el tipo de elemento que es.

print("ACTIVIDAD")
print("\nLista de colores: rojo, azul, verde, amarillo, marron, lila, negro, rosa, blanco, naranja")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores_tupla = tuple(colores)
print("\nImprimimos el tipo de elemento que es: ")
print(type(colores_tupla))

