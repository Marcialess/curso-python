class Motocicleta:
    its_new = True
    motor = False

    def __init__ (self, _color, _matricula, _combustible_litros, _numero_ruedas,
                  _marca, _modelo, _fecha_fabricancion, _velocidad_punta, _peso,_combustible_maximo):
        self.color = _color
        self.matricula = _matricula
        self.combustible_litros = _combustible_litros
        self.numero_ruedas = _numero_ruedas
        self.marca = _marca
        self.modelo = _modelo
        self.fecha_fabricacion = _fecha_fabricancion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso
        self.combustible_maximo = _combustible_maximo

    def arrancar(self):
         if  not self.motor:
            print("El Motor esta Arrancando")
         else:  
            print("El motor ha Arrancado")

    def detener(self):
        if not self.motor:
            print("El motor se ha detenido")
        else: 
            print("El motor Ya estaba detenido")

    def cantidad_combustible(self):
        print(f"Reporte ------->{self.modelo} {self.marca}")
                 

    
CB1 = Motocicleta("Azul","493XX",10,2,"Honda","CB1","17/9/2018","85KMS","118",18)

Sblue = Motocicleta(
    _marca = "Yamaha",
    _modelo = "FZ V-3.0",
    _color = "Azul-matte",
    _numero_ruedas = 2,
    _peso = "137kg",
    _matricula = "PZV-077",
    _combustible_litros = 10,
    _velocidad_punta = 126,
    _combustible_maximo = 18,
    _fecha_fabricancion = "12/07/2021",
      
)     

CB1.precio = 1500
CB1.arrancar()
Sblue.arrancar()
Sblue.precio = 9000

print(f"el precio de la motocicleta {CB1.marca} {CB1.modelo} es de clp$ {CB1.precio}")

#     Para finalizar, crea un nuevo método en la clase, que sea capaz de repostar las motocicletas. Para esto, necesitarás lo siguiente:
# Crea un método para comprobar la cantidad de combustible que tienen las motocicletas. Este servirá para informarnos del estado antes de iniciar el repostaje.
# En este método, se deberá indicar la cantidad de litros que tiene de combustible, la capacidad máxima del tanque de combustible y los litros que faltan para llenar el depósito.
# La salida de este método debe ser una especie de reporte. Pon todo lo anterior y añade un título personalizado con el nombre de la motocicleta que se consulta. Por ejemplo, –> Reporte del depósito de «marca x y modelo x de motocicleta» <–.
# Establecer un tope de depósito que indicaremos especialmente para cada motocicleta con un nuevo atributo. Por ejemplo, la primera tiene una capacidad máxima de 17 litros de combustible. La otra de 20.
# Crear un método que se utilice para poner la cantidad de litros que se quieren repostar. Esto se indicará en la consola por un input().
# Si la cantidad de litros es superior a la de la capacidad que hay en el depósito, se deberá advertir de que no se puede repostar esa cantidad y se le dejará intentarlo de nuevo las veces que haga falta.
# En cambio, si el repostaje es correcto, se indicará en consola la cantidad de litros que tiene la motocicleta.
# No solo hay que indicar la cantidad de combustible que tendrá la motocicleta, tiene que ser efectivo el cambio.

def cantidad_combustible(self):
    print(f"++++ Reporte de la moticicleta {self.marca} {self.modelo}")
    print (f"El tanque tiene {cantidad_combustible} litros")
    print( f"La capacidad máxima del tanque de combustible es de {self.combustible_maximo} litros.")
    print( f"Faltan {self.combustible_maximo - self.combustible_litros} litros para llenar el depósito.")
    print("+++++ Reporte completo")

def cargar_combustible(self):
    while True:
        litros_colocar = float(input('Ingrese la cantidad de litros a cargar'))
        if litros_colocar + self.combustible_litros <= self.maximo_combustible:
            print("Success Completed")
            break
        else:
            print('La cantidad de combustrible a colocar, supera la capacidad maxima')


