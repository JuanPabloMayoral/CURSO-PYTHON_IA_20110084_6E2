# Juan Pablo Mayoral López 20110084 6E2
#Capitulo 14 -Eliminar elementos del() listas en python
#utilizar el método pop() para eliminar únicamente el último elemento de una lista.
print("ACTIVIDAD:")
print("Lista: rojo, azul, verde, amarillo, marron, lila, negro, rosa, blanco, naranja")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#Aqui con la intruccion de POP vamos  a ir elminando posiciones y sus elementos que esten
print("\nVamos a eliminar los colores: azul y blanco")
color1 = colores.pop(1)
color2 = colores.pop(7)
colores_guardados = [color1, color2]
print(colores_guardados)
print("\nAsi queda la nueva lista:")
print(colores)