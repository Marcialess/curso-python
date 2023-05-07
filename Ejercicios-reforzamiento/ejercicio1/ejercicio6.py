# Una jugueteria tiene mucho exito en dos de sus productos: 
# payasos y muñecas.Suele hacer venta por correo y la empresa logistica 
# les cobra por peso de cada paquete asi que deben calcular el peso
# el peso de los payasos y muñecas que saldran en cada paquete a
# demanda. Cada payasos pesa 112g y cada muñeca 75g. escribir un programa 
# que lea el numero de payasos y muñecas vendidos en el ultimo pedido
# y calcule el peso total del paquete que sera enviado.

peso_payaso = 112
peso_muñeca = 75

num_payasos = float(input("Ingrese la cantidad de payaso: "))
num_muñecas = float(input("Ingrese la cantidad de muñecas: "))

calcular_peso_total = (peso_payaso * num_payasos) + (peso_muñeca * num_muñecas)

resultado = calcular_peso_total

print(resultado)