# creating an class
class Transportes:
    pass

# instaciar la clase y crear un objecto
transporte1 = Transportes()

class BuzzLightYear:
    pass

buzz1 = BuzzLightYear()

print(type(transporte1))
print(type(buzz1))

class Droid:
    def __init__(self):
        self.power_on = False


    def switch_on(self):
        print("Hola soy un droid y estoy a tu orden")
        self.power_on = True

    def switch_off(self):
        print("Adios, enciendeme cuando me necesites")    
        self.power_on = False

R3T4K = Droid()
RS21 = Droid()

R3T4K.switch_on()
print("power on R3T4K: ", R3T4K.power_on)
RS21.switch_off()
print("power on RS21: ", RS21.power_on)

class Vehicle:
    def __init__(self,type,model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle('Sedan', 'Voyage')
print(sedan.type_vehicle, sedan.model_vehicle)
Pickup = Vehicle('Pickup', 'KAVAK')
print(Pickup.type_vehicle, Pickup.model_vehicle)




