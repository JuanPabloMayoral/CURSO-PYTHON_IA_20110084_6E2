#Juan Pablo Mayoral López 20110084 6E2
# Capitulo 51 - MANEJO DE EXCEPCIONES EN PYTHON FINAL

print("ACTIVIDAD")

reinicio = True

while reinicio:
    try:
        num1 = int(input("\nIntroduce un numero para hacer una suma\n"))
        num2 = int(input("\nIntroduce un segundo numero para hacer una suma\n"))
    except ValueError:
        print("\nNo has puesto ningun numero amig. intentalo otra vez")
    else:
        print("\nEl resultado es: ", num1 + num2)
    finally:
        pregunta = input("Quieres seguir haciendo mas sumas, Introduce S/N: \n")
    if pregunta == "N":
        reinicio = False
    else:
        print("Decidiste seguir haciendo sumas")
