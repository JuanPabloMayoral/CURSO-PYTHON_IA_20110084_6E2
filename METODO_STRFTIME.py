# Juan Pablo Mayoral L�pez 20110084 6E2
# Capitulo 46 - Como mostrar la fecha actual en python


import datetime, locale

locale.setlocale(locale.LC_ALL, "es-ES")

fecha = datetime.datetime.now()

print(fecha.strftime("%c"))


#print(ahora.strftime("D�a de la semana abreviado: %a "))
#print(ahora.strftime("D�a de la semana completo: %A "))
#print(ahora.strftime("Mes abreviado: %b "))
#print(ahora.strftime("Mes abreviado: %B "))
#print(ahora.strftime("Fecha completa: %c "))
#print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))
#print(ahora.strftime("D�a del mes (01 - 31): %d "))
#print(ahora.strftime("D�a/hora/a�o: %D "))
#print(ahora.strftime("D�a del mes (1 - 31): %e "))
#print(ahora.strftime("A�o en dos d�gitos: %g "))
#print(ahora.strftime("A�o en cuatro d�gitos: %G "))
#print(ahora.strftime("Mes abreviado: %h "))
#print(ahora.strftime("Hora (00 - 23): %H "))
#print(ahora.strftime("Hora (01 - 12): %I "))
#print(ahora.strftime("D�a del a�o: %j "))
#print(ahora.strftime("Mes del 01 al 12: %m "))
#print(ahora.strftime("Minuto: %M "))
#print(ahora.strftime("Salto de l�nea: %n"))
#print(ahora.strftime("AM o PM: %p "))
#print(ahora.strftime("Hora + AM o PM: %r"))
#print(ahora.strftime("Hora y minutos: %R"))
#print(ahora.strftime("Segundos: %S"))
#print(ahora.strftime("Tabulaci�n: %t"))
#print(ahora.strftime("Hora, minutos y segundos: %T"))
#print(ahora.strftime("D�a de la semana (n�mero): %u"))
#print(ahora.strftime("Semana del a�o (empieza en domingo): %U"))
#print(ahora.strftime("Semana del a�o(Condiciones especiales): %V"))
#print(ahora.strftime("Semana del a�o (empieza en lunes): %W"))
#print(ahora.strftime("D�a de la semana (empieza en domingo): %w"))
#print(ahora.strftime("D�a/mes/a�o de dos d�gitos: %x"))
#print(ahora.strftime("Hora/minutos/segundos: %X"))
#print(ahora.strftime("A�o corto: %y"))
#print(ahora.strftime("A�o largo: %Y"))