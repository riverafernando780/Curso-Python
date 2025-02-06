class mascotas():
    def sonido(self):
        pass

class gato(mascotas):
    def sonido(self):
        print("meow")
        
class perro(mascotas):
    def sonido(self):
        print("wof")
#Las dos clases anteriores heredan de la clase mascota y tienen un metodo sonido
        
def Sonido(mascota):#Esta función como el ejemplo anterior nos permitira usar el polimorfismo
    mascota.sonido()

napolitana=gato()
brownie=perro()
Sonido(napolitana)#Se usa el sonido de gato
Sonido(brownie)#Se usa el sonido de perro