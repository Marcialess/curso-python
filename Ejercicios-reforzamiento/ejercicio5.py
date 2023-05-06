# Ejercio5

cantidad_invertida = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual : "))
num_anios = int(input("Ingrese el número de años: "))

capital_obtenido = cantidad_invertida * (1 + (interes_anual/100))**num_anios

print("El capital obtenido es de:", round(capital_obtenido, 2), "Pesos")