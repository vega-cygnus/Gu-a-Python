peso = input("¿Cuánto pesas (kg)? ")
estatura = input("¿Cuánto mides (metros)?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))