# Ejercicio 4
horas_trabajadas = float(input("Ingrese la cantidad de horas: "))
coste_hora = float(input("Ingrese el valor de la hora: "))                         

valor_hora_total = coste_hora * horas_trabajadas

print(f'Tu salario es: {valor_hora_total}')



cantidad_invertida = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (%): "))
num_anios = int(input("Introduce el número de años: "))

capital_obtenido = cantidad_invertida * (1 + (interes_anual/100))**num_anios

print("El capital obtenido es de:", round(capital_obtenido, 2), "Pesos")