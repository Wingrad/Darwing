print("bienvenid@")
print("para salir escriba 'salir' ")

while True:
    operacion = input("quiere sumar, restar, multiplicar o dividir? ")
    if operacion.lower() == "salir":
        print("byeeee")
        break


    numero1 = float(input("escriba el primer numero"))
    numero2 = float(input("escriba el segundo numero"))

    if operacion.lower() == "sumar":
        resultado = numero1 + numero2
        print("El resultado de la suma es:", resultado)
    
    elif operacion.lower() == "restar":
        resultado = numero1 - numero2
        print("El resultado de la resta es:", resultado)
    
    elif operacion.lower() == "multiplicar":
        resultado = numero1 * numero2
        print("El resultado de la multiplicacion es:", resultado)
    elif operacion.lower() == "dividir":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("El resultado de la division es:", resultado)
        else:
            print("que tonto no puedes dividir 0")
    else:
        print("upps un mini error")