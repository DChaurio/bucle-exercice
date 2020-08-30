#Escriba un programa que pida dos números enteros y escriba qué números son pares y búsquedas impares desde el primero hasta el segundo.

    imprimir ("PARES E IMPARES")
    numero_1 = int (input ("Escriba un número entero:"))
    numero_2 = int (input (f "Escriba un número entero mayor o igual que {numero_1}:"))

    si numero_2 <numero_1:
        print (f "¡Le he pedido un número entero mayor o igual que {numero_1}!")
    más:
        para i en rango (numero_1, numero_2 + 1):
            si i% 2 == 0:
                print (f "El número {i} es par.")
            más:
                print (f "El número {i} es impar.")
              
#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
              
    imprimir ("DIVISORES")
    numero = int (input ("Escriba un número entero mayor que cero:"))

    si numero <= 0:
        print ("¡Le he pedido un número entero mayor que cero!")
    más:
        print (f "Los divisores de {numero} son", end = "")
        para i en el rango (1, numero + 1):
            si numero% i == 0:
                print (i, end = "")
                
#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
                
    imprimir ("MAYORES QUE EL ANTERIOR")
    valores = int (input ("¿Cuántos valores va a introducir?"))
    si valores <1:
        print ("¡Imposible!")
    más:
        anterior = int (input ("Escriba un número:"))
        para i en el rango (valores - 1):
            numero = int (input (f "Escriba un número más grande que {anterior}:"))
            si numero <= anterior:
                print (f "¡{numero} no es mayor que {anterior}!")
            anterior = numero
        print ("Gracias por su colaboración.")