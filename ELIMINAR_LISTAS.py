# Juan Pablo Mayoral López 20110084 6E2
#Capitulo 12 -Eliminar elementos del() listas en python
#Eliminar cierto elementos de una lista predeterminada
print("ACTIVIDAD:")
print("Lista: rojo, azul, verde, amarillo, marron, lila, negro, rosa, blanco, naranja")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#Aqui con la intruccion de del vamos  a ir elminando posiciones y sus elementos que esten
print("\nVamos a eliminar los colores: azul, marron, negro, rosa")
del colores[1]
del colores[3]
del colores[4]
del colores[-3]
print("\nAsi queda la nueva lista:")
print(colores)