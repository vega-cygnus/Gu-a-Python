dividendo = float(input("Por favor, ingresa el dividendo: "))
divisor = float(input("Por favor, ingresa el divisor: "))

if divisor == 0:
    print("Error: No se puede dividir por cero.")
else:
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)