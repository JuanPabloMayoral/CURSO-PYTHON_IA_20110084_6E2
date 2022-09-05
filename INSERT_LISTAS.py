# Juan Pablo Mayoral López 20110084 6E2
#Capitulo 16 - Como insertar eementos en listas python con el metodo insert()
#Añadir a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. Deberás hacer esto utilizando posiciones de lista negativas.

print("ACTIVIDAD")
print("\nLista de colores: rojo, verde, amarillo, marron, lila, negro, rosa, blanco, naranja")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("\nAgregamos el color magenta y turquesa")
colores.insert(-4, 'magenta')
colores.insert(-1, 'turquesa')
print("\nEsta es la nueva lista: ")
print(colores)