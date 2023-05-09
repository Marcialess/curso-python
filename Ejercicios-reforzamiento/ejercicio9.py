# Escribir un programa que pida al usuario dos numeros y muestre 
#  por pantalla su division. si el divisor es cero el programa 
#  debe decir que no se puede dividir.


numerador = int(input("Ingrese el numero: "))
denominador = int(input("Ingrese el denominador: "))

if denominador == 0:
    print("No se puede dividir")
else:
    resultado = numerador/denominador
    print(f"El resultado es: {resultado}")

