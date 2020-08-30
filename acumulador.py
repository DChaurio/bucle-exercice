#Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo.


    print("NÚMERO PRIMO")
    numero = int(input("Escriba un número entero mayor que 1: "))

    if numero <= 1:
        print("¡Le he pedido un número entero mayor que 1!")
    else:
        contador = 0
        limite = round(numero ** 0.5)
        for i in range(1, limite + 1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 1:
            print(f"{numero} es primo.")
        else:
            print(f"{numero} no es primo.")
