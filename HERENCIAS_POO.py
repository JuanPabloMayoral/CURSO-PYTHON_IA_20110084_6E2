# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 41 - Que es la herencia de clases python

class Personas:
    def __init__(datos, nombre, edad):
     datos.nombre = nombre
     datos.edad = edad 
        
    def muestra_datos(datos):
      print("El nombre de la persona es: " + datos.nombre, "y tiene", datos.edad)

persona1 = Personas("Juan Pablo", 21)

persona1.muestra_datos()

class Personas_premium(Personas):
    pass


persona2 = Personas_premium("Ana", 28)

persona2.muestra_datos()