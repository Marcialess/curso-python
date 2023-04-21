first_name = "Marcial";
last_name = "Abad";
print(first_name + " " + last_name);

mensaje = "Hola " * 3;
print(mensaje);

# concatenando Stings

mensaje3 = "Dayana"
mensaje3 += ", Martinez"
print (mensaje3)
# utilizando la function bult in len encuentra la cantidades de caracteres;
print(len(mensaje3));

cadena = "esto es una cadena para realizar una prueba" 
posicion = cadena.find("simular")
test1 = cadena.find("realizar ")
print(test1)
print(posicion)


Mayus = "Cambiando todas mis Letras en mINUSCULA"
print(Mayus.lower())

Idog = "hi im a dog, i like my dog"
print(Idog.replace("dog", "cat"))

empty_list = []
print(empty_list)

full_filed_list = [1, 3, 500, 1.4, [2,"a"], {"name": "Marcial"},(1,20,33)]
print(full_filed_list)

second_list = list()
print(second_list)

print(list("dayana"))

range_one = range(50)
print(list(range_one))

# agregando un item a la lista
numeros = [1,41,23,337]
numeros.append(17)
print(numeros)

print(numeros[2])

#iterar una lista
for element in  numeros:
    print(element)

# eliminar un elemento de la lista
my_list = [1, 2, 3, 4, 5]

del my_list[0]
print(my_list)

# modificar la lista

mi_lista = [1, 2, 3, 4, 5]
mi_lista[2] = 6
print(mi_lista)

fullfilled_tuple = ("simply",47,"happiness")
empty_tuple = ()
print (fullfilled_tuple,empty_tuple)

new_tuple = ('simbol',)
print(type(new_tuple))

verduras = tuple()

list_to_convert = ['tomate','cebolla','pimentos']
tuple_converted = tuple(list_to_convert)
print(tuple_converted, verduras)


tuple3 = ('Alvarez','Abad','Amengual','Angus')
tuple3.sort('Alvarez','Abad')
print(tuple3)