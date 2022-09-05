# Juan Pablo Mayoral López 20110084 6E2
#Capitulo 17 - Como ordenar elementos con sort() y sorted() en listas para python
#Ordenar la siguiente lista en orden alfabético descendente (de la letra 'z' a la 'a').

print("ACTIVIDAD")
print("\nLista de colores: rojo, azul, verde, amarillo, marron, lila, negro, rosa, blanco, naranja")
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron',
          'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("\nVAMOS A ORDENARLO POR ORDEN ALFABETICO DESCENDENTE")
colores.sort(reverse=True)
print("\nLa nueva lista queda: ")
print(colores)