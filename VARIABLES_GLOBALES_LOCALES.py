# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 43 - Variables globales, locales y funciones anidadas en python

#Se declara una variable dentro de una funcion y se crea otra funcion para cambiar el valor de la variable creada en la primer funcion
print("ACTIVIDAD 1")
def funcion1():
    v1 = "La variable esta dentro de la funcion"
    print(v1)
    def funcion2():
        v1 = "Se ha cambiado el valor de la funcion"
        print(v1)
    funcion2()

funcion1()
#Se declara el valor 60 en la variable num y se agrega a una funcion llamandola con la palabra global
print("ACTIVIDAD 2")

num = 50
def funcion1():
    global num1
    num1 = 20

funcion1()

print(num1)