# Juan Pablo Mayoral López 20110084 6E2
# Capitulo 37 - Como crear clases en python con la palbra reservada class

class Avion():
    peso = 2500
    largo = 50
    ancho = 20
    color1 = "Negro"
    color2 = "Plateado"
    motores = 4
    activada = False
    compuerta_principal = False
    sistema_defensa = True
    autodestruccion = False

    def encender(self):
        self.activada = True

    def apagar(self):
        self.activada = False

    def abrir_compuerta(self):
        self.compuerta_principal = True

    def cerrar_compuerta(self):
        self.compuerta_principal = False

    def desactivar_defensas(self):
        self.sistema_defensa = False

    def activar_defensas(self):
        self.sistema_defensa = True

    def activar_autodestrucion(self):
        self.autodestruccion = True
        mensaje = "El avion se autodestruira en 1 minuto..."
        print(mensaje)

    def estado_motores(self):
        if (self.activada):
            return "Motores a toda potencia."
        else:
            return "Se apagaron los motores."

    def estado_compuerta(self):
        if (self.compuerta_principal):
            return "La compuerta se ha abierto."
        else:
            return "La compuerta de ha cerrado."

    def estado_defensa(self):
        if (self.sistema_defensa):            
            return "Todas las armas estan listas."
        else:
            return "Peligro esta indefenso capitan."
    
#Se crea el objeto nave1 perteneciente a la clase Naves.
    
f14=Avion()

#Comandos (llamadas) al objeto.

#Enciende nave.
f14.encender()

#Comprueba estado de los motores.
print(f14.estado_motores())

#Apaga nave.
f14.apagar()

#Comprueba estado de los motores.

print(f14.estado_motores())

#Abre la compuerta.
f14.abrir_compuerta()

#Comprueba el estado de la compuerta.
print(f14.estado_compuerta())

#Cierra compuerta.
f14.cerrar_compuerta()

#Comprueba el estado de la compuerta.
print(f14.estado_compuerta())

#Comprueba el estado de la defensas.
print(f14.estado_defensa())

#Desactiva las defensas.
f14.desactivar_defensas()

#Comprueba el estado de la defensas.
print(f14.estado_defensa())

#Ejecuta la autodestrucción de la nave.
f14.activar_autodestrucion()