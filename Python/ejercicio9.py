pan_viejo = int(input("¿Cuántas barras de pan de ayer quiere llevar? "))
precio = 3.49 
descuento = 0.6
coste = pan_viejo * precio * (1 - descuento)
print("El precio habitual de una barra fresca es " + str(precio) + "pesos")
print("El descuento por cada una barra no fresca es del " + str(descuento * 100) + "%")
print("El total de su compra es de " + str(round(coste, 2)) + "€")