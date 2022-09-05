# Juan Pablo Mayoral L�pez 20110084 6E2
# Capitulo 42 - Que es la herencia de clases python

class Personas:
    def __init__(datos, nombre, edad):
     datos.nombre = nombre
     datos.edad = edad 
        
    def muestra_datos(datos):
      print("El nombre de la persona es: " + datos.nombre, "y tiene", datos.edad)

persona1 = Personas("Juan Pablo", 21)

persona1.muestra_datos()

class Personas_premium(Personas):
    def __init__(datos, nombre, edad, instagram):
        Personas.__init__(datos,nombre,edad)
        datos.instagram = instagram
    
    def muestra_datos_premium(datos):
        print("El nombre de la persona es: " + datos.nombre, "y tiene", datos.edad, "Su instagram es:", datos.instagram)

persona2 = Personas_premium("Ana", 28, "Anna_12")

persona2.muestra_datos_premium()