# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 40 - Como declarar clases vacias con pass y eliminar objetos

class Personas:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def muestra_datos(self):
        print("El nombre de la persona es: " + self.nombre, self.edad)
              
              
persona1 = Personas("Juan Pablo", 21)

print(persona1.nombre, persona1.edad)

del persona1.edad

print(persona1.nombre, persona1.edad)