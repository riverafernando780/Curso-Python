class laptop():
    def __init__(self):
        self.__teclado=True
        self.__graficos="Integrados"
        self.__procesador="Intel"
        self.__pantalla="Normal"
        self.__ram=8
    def boton_OnOf(self,power):
        self.__encender=power
        """Note que es posible definir atributos de una clase mas alla del contructor, aunque no es recomendable ya que es mejor 
        si todos los atributos de la clase son definidos en los constructores"""        
        if self.__encender:
            return "Computadora encendida"
        else:
            return "Computadora apagada"
    def reconfigurar(self):
        self.__graficos=input("Ingrese el tipo de graficos(integrados/nvidia):\n")
        self.__procesador=input("Ingrese el procesador que desa tener:(intel/amd):\n")
        self.__EstatusFabricante()
        
    def __EstatusFabricante(self):
        """Hemos encapsulado este metodo pues emula un estatus de validación que solo se puede habilitar cuando hay cambio de 
        componentes(procesadores o tarjetas graficas)"""
        print("Las reconfiguraciones fueron realizadas\nGraficos: ",self.__graficos,", Procesador: ",self.__procesador)

laptop1=laptop()
a=input("Encender computadora?(s/n)")
if a=="s":
    print(laptop1.boton_OnOf(True))
else:
    print(laptop.boton_OnOf(False))
    
laptop1.reconfigurar()