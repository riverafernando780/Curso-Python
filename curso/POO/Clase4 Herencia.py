class electrodomesticos():
    def __init__(self,marca):
        self.__energizado=False
        self.__marca=marca
        self.__encendido=False
    def enchufar(self):
        self.__energizado=True
    def encender(self):
        power=input("Desea encender el dispositivo(s/n)")
        if power=="s":
            self.__encendido=True
        else:
            self.__encendido=False
        if self.__encendido:
            print("El dispositivo se ha encendido")
        else:
            print("El dispositivo se encuentra apagado")
    def status(self):
        print("El dispositivo de marca: ",self.__marca,"\nEnergizado: ",self.__energizado,"\nEncendido: ",self.__encendido)

class lavadora(electrodomesticos):
    """La Herencia se da cuando al contruir un nuevo objeto usamos como parametro la clase de la que queremos heredar,
      en este caso nuestra nueva clase lavadora, ha heredado de la clase electrodomesticos"""
    pass#La instruccion pass, le indica al programa que pase de largo, es una forma de decir "esta vacio"

Lavadora=lavadora("mabe")#El constructor es el mismo de electrodomesticos
Lavadora.enchufar()#Contamos con los mismos metodos
Lavadora.status()