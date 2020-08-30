def main():
    from random import randrange
    print("CÁLCULO ESTIMADO (3)")
    
    preguntas = int(input("Número de preguntas: "))

    if preguntas < 1:
        print("El número de preguntas debe ser al menos 1.")
    else:
        correctas=0
        for i in range(preguntas):
            b=randrange(11,99)
            a=randrange(11,99)
            
            intento = int(input(f"¿Cuánto es {a} x {b}?"))

            resultado=a*b

            if intento==resultado:               
                print("Lo lograste!")
                correctas+=1
                
            elif resultado*0.9<intento<resultado*1.1:
                print(f"¡Ha fallado por menos del 10%! La respuesta correcta era {resultado}.")
                correctas+=0.66

            elif resultado*0.7<intento<resultado*1.3:
                print(f"¡Ha fallado por menos del 30%! La respuesta correcta era {resultado}.")
                correctas+=0.33

            else:
                print(f"¡Ha fallado por más del 30%! La respuesta correcta era {a * b}.")    
                
        nota=preguntas/correctas

        print(f"Le corresponde una nota de {nota}")

        if nota>=9:
            print("Felicidades, excelente promedio")

        

if __name__ == "__main__":
    main()