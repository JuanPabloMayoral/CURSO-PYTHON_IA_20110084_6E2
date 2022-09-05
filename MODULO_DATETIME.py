# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 45 - Trabajar con fechas con el modulo datetime en python
import datetime
#En esta actividad pondremos la manera mas facil de declarar la funcion datetime
print("\nActividad1")

fecha = datetime.datetime.now()

print(fecha)
#Aqui ordenaremos un poco mas la manera de imprimir la fecha y hora declarando las variables
print("\nActividad2")

fecha = datetime.datetime(2022, 9, 4, 10, 50, 45)

print(fecha)
#Aqui pondremos con un string especificando el año, dia y mes
print("\nActividad3")

fecha = datetime.datetime.now()

print("Year:",fecha.year)
print("Mes:",fecha.month)
print("Dia:",fecha.day)