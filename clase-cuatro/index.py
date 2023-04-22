# TEMA: Diccionario

# Orden en las claves
# Son Mutables
# Claves ser unicas
# Son de muy rapido acceso.

empty_dict ={}

fullFiled_dict ={
    "id":1,
    "name": "Marcial"
}

print(fullFiled_dict)

lista_1 = ['a1', 'b2']
dict_converterd = dict(lista_1)
print(lista_1, dict_converterd)

tuple_1 = ('a1','b2')
print(tuple_1, dict(tuple_1))

list_dimensional = [['a',1],['b',3]]
print(list_dimensional,dict(list_dimensional))

# 
d = {'uno': 1, 'dos': 2}
print(d)


# Añade un nuevo elemento al diccionario
d['tres'] = 3
print(d)

# Obteniendo un elemento de la lista del diccionario

dictionary = {
    "Santiago": "Chile",
    "Caracas": "Venezuela",
    "Bogota": "Colombia",
    "Rio de Janeiro": "Brasil"
}






empty_dict_2 = dict()
print(empty_dict_2)

fullFiled_dict_2 = dict(
genero = "M",
nacionalidad = "Venezolana"
)
print(fullFiled_dict_2)

Empleados = {
    "Nombre": "Dayana",
    "Apellido": "Martinez",
    "Edad": "33",
    "RUT": "26.122.212-4"
}
# for con el metodo values()
for testv in Empleados.values(): 
        print(testv)

# for con el metodo items
for testvo in Empleados.items():
        print(testvo)


        suministro = True
        if suministro == False:
                print("Estos son verduras")
        else:
                print("esto no son suministros de verduras")

                #utilizando la condicional if con el ellif

Dayana = 3



# como puedo ejecutar ejercio para practicar: escriba un programa que permita adivinar
#  un personaje de Marvel en base a estas preguntas:
# 1 ¿ Puede Volar?
# 2 ¿ Es Humano ?
# 3 ¿ Tiene Mascara?

# volar = 'si'
# humano = 'si'
# mascara = 'si'

# if personaje1 == 1:
#     print(' El personaje es Iroman')
# elif personaje1 > 1:
#         print('El personaje es Wanda ')
# else: print('No es un personaje de Marvel')
        
# print("Bienvenido al juego de adivinanza de personajes de Marvel!")
# print("Responda las siguientes preguntas con sí o no")

puede_volar = False
# es_humano = True
# tiene_mascara = True

# if puede_volar == "sí" and es_humano == "no" and tiene_mascara == "sí":
#     print("¡El personaje a adivinar es Iron Man!")
# elif puede_volar == "sí" and es_humano == "no" and tiene_mascara == "no":
#     print("¡El personaje a adivinar es Thor!")
# elif puede_volar == "no" and es_humano == "sí" and tiene_mascara == "sí":
#     print("¡El personaje a adivinar es Spider-Man!")
# elif puede_volar == "no" and es_humano == "sí" and tiene_mascara == "no":
#     print("¡El personaje a adivinar es Captain America!")
# else:
#     print("Lo siento, no he podido adivinar el personaje.")


# trabajando con ciclos
# ciclo WHILE

want_exit = 'n'
while want_exit == 'n':
      print("Hola Todo bien")
      want_exit = input("¿Quieres Salir S/N?")

print("Fuera del while")


print('=====segundo While=====')

num_question = 0
want_exit = 'n'
while want_exit == 'n':
      print("Hola Todo bien")
      want_exit = input("¿Quieres Salir S/N?")
      num_question += 1
      if num_question == 4:
             print('Se acabo todo el numero de intentos')
             break

print("Fuera del while")