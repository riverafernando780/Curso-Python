"""
ORIGINALMENTE LAS PROPIEDADES DE Armadura ESTABAN ENCAPSULADAS, SIN EMBARGO YA QUE LA CLASE Space SOBRESCRIBIMOS EL 
METODO ESTATUS ESTE PASA A SER AHORA METODO DE LA CLASE SPACE Y LOS ATRIBUTOS ENCAPSULADOS SOLO SON ACCESIBLES DESDE 
LOS METODOS DE LA CLASE ARMADURA Y NO SE PUEDE ACCEDER DESDE CLASE HIJOS
"""
class Armadura():
    def __init__(self,version,arc):
        self.reactor=arc
        self.version=version
        self.nrepulsores=2
        self.enlinea=True
    def estatus(self):
        if(self.enlinea):
            print("Armadura en linea\nReactor arc: ",self.reactor,"\nVersion del traje: ",self.version
                  ,"\nEl numero de repulsores es: ",self.nrepulsores)
        else:
            print("El traje no esta en linea se recomienda reinicio")
    def reinicio(self):
        print("Reinicio del sistema en progreso......")
        self.enlinea=True
        self.estatus()
    def dagno(self):
        self.enlinea=False
        
"""print("Saludos, soy Jarvis, a contunuación seleccione un traje de armería")
v=input("Ingrese la versión del traje: ")
reactor=bool(input("Dotara al traje de un reactor de arco(de no hacerlo solo se usara la carga de la placa o nodo central)"
                   +"\n(ingrese 1->reactor arc o 0-> sin reactor): "))
mk=Armadura(v,reactor)
mk.estatus()
print("---------------------------------------------------------------------------------------------------------------------------------")
mk.dagno()
mk.estatus()
print("---------------------------------------------------------------------------------------------------------------------------------")
mk.reinicio()"""
class Space(Armadura):#Nuevamente usamos la herencia
    orbita="En tierra"#Hemos agregado una nueva caracteristica
    def Poner_en_orbita(self):
        self.orbita="En orbita"
    def estatus(self):#Fue necesario sobreescribir el metodo de estatus para mostrar si el traje esta en el espacio
        if(self.enlinea):
            print("Armadura en linea\nReactor arc: ",self.reactor,"\nVersion del traje: ",self.version
                  ,"\nEl numero de repulsores es: ",self.nrepulsores,"\nLa armadura esta en: ",self.orbita)
        else:
            print("El traje no esta en linea se recomienda reinicio")
print("---------------------------------------------------------------------------------------------------------------------------------")
SpaceArmor=Space("model 1",False)
SpaceArmor.estatus()
SpaceArmor.Poner_en_orbita()
print("---------------------------------------------------------------------------------------------------------------------------------")
SpaceArmor.estatus()

class ArmasMagicas():
    uru=True
    def __init__(self,):
        self.encantamiento="Encantada por Odin"

class MysticArmor(Armadura,ArmasMagicas):
    """
    Estamos ocupando herencia multiple, al tener como primer parametro la clase armadura el interprete de python designa como 
    contructor a esta clase precisamente el CONSTRUCTOR DE ARMADURA y no el de ArmasMagicas
    """
    pass

Iron_Destroyer=MysticArmor("Bleeding Edge",1)
Iron_Destroyer.estatus()
print(Iron_Destroyer.uru)
"""
Iron destroyer es una MysticArmor que hereda precisamente de Armas magicas, en particular sus atributos por ende tiene el atributo uru
Note que para la linea 73 si se descomenta dara error pues el atributo encantamiento esta condicionado a existir por el constructor 
y ya que el contructor que se utiliza es precisamente el de Armaduras, nunca se gana este atributo
"""
#print(Iron_Destroyer.encantamiento)