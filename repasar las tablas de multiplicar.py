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
        

#Amplíe el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas e incorrectas e indique la nota correspondiente. Si la nota es igual o mayor que 9, el programa felicitará al usuario por el resultado.
    
    from random import randrange
    
    print("TABLAS DE MULTIPLICAR (3)")
    preguntas = int(input("Número de preguntas: "))
    if preguntas < 1:
        print("El número de preguntas debe ser al menos 1.")
    else:
        correctas = 0
        for _ in range(preguntas):
           
            a = randrange(2, 11)
            b = randrange(2, 11)
            respuesta = int(input(f"¿Cuánto es {a} x {b}? "))
            if respuesta == a * b:
                print("¡Respuesta correcta!")
                correctas += 1
            else:
                print("¡Respuesta incorrecta!")

       
        if correctas == 1:
            print(f"Ha contestado correctamente 1 pregunta.")
        else:
            print(f"Ha contestado correctamente {correctas} preguntas.")
        nota = round(correctas / preguntas * 10, 1)
        print(f"Le corresponde una nota de {nota}.")
        if nota >= 9:
            print("felicidades, excelente promedio")
                



