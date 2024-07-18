peso_engrane = 112
peso_cilindro = 75
total_engranes = int(input("Introduce la cantidad de engranes que se enviarán: "))
total_cilindros = int(input("Introduce el número de cilindros a enviar: "))
peso_total = peso_engrane * total_engranes + peso_cilindro * total_cilindros
print("El peso total del paquete en kilogramos sería: " + str(peso_total))