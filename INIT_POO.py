# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 38 - Ques el metodo init


class Personas():
    
    def __init__(self, nombre, registro):
        self.nombre = nombre 
        self.registro = registro
        
    def saludo(self):
        print("Hola" +self.nombre+ " Iniciaste sesion correctamente \n")

    def despedida(self):
        print(self.nombre + ", acabas de cerrar sesion \n")



persona1=Personas("Carlos", "22378")

persona2=Personas("Alberto","92732")

persona1.saludo()
persona2.saludo()
persona1.despedida()
persona2.despedida()
