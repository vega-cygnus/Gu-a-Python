numero = int(input("Por favor, ingresa un número: "))

if numero <= 0:
    print("Recuerda que debe ser entero y positivo.")
else:
    numeros_impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
    resultado = ", ".join(numeros_impares)
    print("Aquí tienes una lista de los números impares desde 1 hasta", numero, ":", resultado)