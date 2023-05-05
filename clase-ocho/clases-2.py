class Motos:
    def __init__(self,name,model,cilindrada):
        self.name = name
        self.model = model
        self.cilindradad = cilindrada

yamaha = Motos("FZ","3.0","150cc")



class Droid:
    def __init__(self,name):
        self.hidden_name = name

    @property
    def name(self) -> str:
        return self.hidden_name

    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name
    
android = Droid("Artur")
print(android.name)
android.name = "k2k"    
print(android.name)

android.hidden_name = "Verde"
print(android.hidden_name)
print(android.name)

class CalculatedValue:
    def __init__(self,name,height):
        self.name = name
        self.height = height

    @property
    def get_calculated_value(self) -> float:
        return 0.35 * self.height

valuex = CalculatedValue("ratio", 10)
print(f"El {valuex.name} es: {valuex.get_calculated_value}")

print("\n=============\n")

class Dog:
    obeys_owners = True

    def __init__(self,_name):
        self.name = _name

dog_one = Dog("Canela")
dog_two = Dog("Peluche")
dog_three = Dog("Muñeco")

print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owners}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owners}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owners}')

print("\n=============\n")

dog_one.obeys_owners = False
dog_two.obeys_owners = False
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owners}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owners}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owners}')



