def first_function(name):
    print(f'hola soy una funcion llamada {name}')

first_function('Marcial')

def second_function(first_name,last_name):
    print(f'Hola es mi nombre y apellido {first_name}, {last_name}')
second_function(last_name='Abad', first_name='Marcial')  

def multiplicar_texto(text,multiplier = 2):
    print(text*multiplier)


multiplicar_texto("*")


def varibilidad(param1,param2,**others):
    print(param1)
    print(param2)
    print(others)
varibilidad(3,"cuarenta", id = 0, name= 'carlos')