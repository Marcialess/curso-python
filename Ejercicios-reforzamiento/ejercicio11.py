# # Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
# # Nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M
# Y a los hombres con un nombre posterior a la N y el grupo B por el resto.
#  Escribir un programa que pregunte al usuario su nombre y sexo, y muestre
# por pantalla el grupo que le corresponde


name = str(input("Ingrese su nombre: "))
sexo = str(input("Ingrese su sexo: "))

if (sexo == "M" and name < "M") or (sexo == "H" and name > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f'Tu nombre es {name}, tu sexo es {sexo}, perteneces al grupo {grupo}')

