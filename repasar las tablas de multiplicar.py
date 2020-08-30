#A. Repasar las tablas de multiplicar

#Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta.


from random import randrange


    print("TABLAS DE MULTIPLICAR (1)")

    a = randrange(2, 11)
    b = randrange(2, 11)
    respuesta = int(input(f"¿Cuánto es {a} x {b}? "))

    if respuesta == a * b:
        print("¡Respuesta correcta!")
    else:
        print("¡Respuesta incorrecta!")


