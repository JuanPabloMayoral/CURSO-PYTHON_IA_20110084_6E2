# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 39 - Ques es self - cambiar valores en objetos


class Personas:
    def __init__(persona, nombre, edad):
        persona.nombre = nombre
        persona.edad = edad
    def muestra_datos(datos):
        print("El nombre y edad de la persona es: \n" + datos.nombre, datos.edad)
        
   



persona1 = Personas ("Juan Pablo", 21)
persona1.muestra_datos()





