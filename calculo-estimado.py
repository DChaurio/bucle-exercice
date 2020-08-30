""Escriba un programa que genere una multiplicación de dos números del 11 al 99 al azar,
pregunte por el resultado y diga si se ha dado la respuesta correcta, si está a menos del
10% del valor correcta o a menos del 30%."

    from random import randrange
    
    print("CÁLCULO ESTIMADO (1)")
    a = randrange(11, 100)
    b = randrange(11, 100)

    respuesta = int(input(f"¿Cuánto es {a} x {b}? "))

    if respuesta == a * b:
        print("¡Respuesta correcta!")
    elif (a*b)*0.9<respuesta<(a*b)*1.1:
        print(f"¡Ha fallado por menos del 10%! La respuesta correcta era {a * b}.")
    elif (a*b)*0.7<respuesta<(a*b)*1.3:
        print(f"¡Ha fallado por menos del 30%! La respuesta correcta era {a * b}.")
    else:
        print(f"¡Ha fallado por más del 30%! La respuesta correcta era {a * b}.")
        
#Amplíe el programa anterior haciendo que el programa pida primero al usuario cuántas multiplicaciones se van a plantear.

    from random import randrange
    print("CÁLCULO ESTIMADO (2)")
    cantidad = int(input("Número de preguntas: "))

    if cantidad < 1:
        print("El número de preguntas debe ser al menos 1.")
    else:
        for i in range(cantidad):
            a = randrange(11, 100)
            b = randrange(11, 100)
            
            respuesta = int(input(f"¿Cuánto es {a} x {b}? "))
            
            if respuesta == a * b:
                print("¡Respuesta correcta!")
            elif (a*b)*0.9<respuesta<(a*b)*1.1:
                print(f"¡Ha fallado por menos del 10%! La respuesta correcta era {a * b}.")
            elif (a*b)*0.7<respuesta<(a*b)*1.3:
                print(f"¡Ha fallado por menos del 30%! La respuesta correcta era {a * b}.")
            else:
                print(f"¡Ha fallado por más del 30%! La respuesta correcta era {a * b}.")
        
