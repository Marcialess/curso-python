# Escriba una clase MobilePhone que represente un telefono movil.
# Atributos
# manufacturer ( cadena de texto)
# screen_size (flotante)
# apps (lista de cadenas de texto)
# status (false: apagado, True: encendido)
# Metodos
# _init_(self, manufacturer, screen_size, num:cores)
#power_on(self)
#power_off(self)
# install_app(self, app)
#uninstall_app(dels, app

class MobilePhone:
    
    def __init__(self,manufacturer,screen_size,num_cores,apps,status=False):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False
        


    def power_on(self):
        self.status = True
        print("Hola Bienvenido")

    def power_off(self):
        self.status = False
        print("Good Bye")    

    def install_apps (self,apps):
        self.apps.append(apps)

    def uninstall_apps(self,apps):
        self.apps.remove(apps)    
    
        
        
     
PhoneAndroid = MobilePhone (
    manufacturer="China",
    screen_size= 9.1,
    num_cores=8,
    apps=[],
    )

PhoneAndroid.install_apps("Spotify")
PhoneAndroid.install_apps("Facebook")
PhoneAndroid.install_apps("Instagram")
print(PhoneAndroid.apps)

PhoneAndroid.uninstall_apps("Spotify")
print(PhoneAndroid.apps)


    
        
        