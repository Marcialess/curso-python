import random
# altura = int(input("dime la altura del triangulo: "))
# repeat = range(altura)

# triangulo = ""
# for i in repeat:
#         triangulo += "*"
#         print(triangulo)
    
# print("n/==============/n")

    # Ejercicio : Escribir un programa que almacene la cadena de caracteres contraseña
    # en una variable, pregunte al usuario por la contraseña que introduzca la contraseña correcta.


# contraseña = input("Introduzca su contraseña: ")
# clave = ("d10s")
# while contraseña != clave:
#         contraseña = input("Introduzca su contraseña: ")
# if contraseña == clave:
#             print("Bienvenido")
        




turno = 1
playerA = {'nombre': 'JugadorA',
           'vida': 50,
           'Ataque': 18}
playerB = {'nombre': 'Jugador B',
           'vida': 50,
           'Ataque': 18}

numeroAleatorio = random.randint(1, 10)
numero = 5

if numeroAleatorio > numero:
    print(playerA['nombre'] + " comenzará el combate.")
else:
    print(playerB['nombre'] + " comenzará el combate.")

while True:
    # Si es el turno del jugador A
    if turno == 1:
       print(playerA['nombre'] + " tiene " + str(playerA['vida']) + " vida.")