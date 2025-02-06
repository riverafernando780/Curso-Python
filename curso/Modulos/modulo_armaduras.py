class Armadura():
    def __init__(self,version,arc):
        self.reactor=arc
        self.__version=version#Hemos encapsulado propiedades que no se deberian alterar
        self.__nrepulsores=2
        self.enlinea=True
    def estatus(self):
        if(self.enlinea):
            print("Armadura en linea\nReactor arc: ",self.reactor,"\nVersion del traje: ",self.__version
                  ,"\nEl numero de repulsores es: ",self.__nrepulsores)
        else:
            print("El traje no esta en linea se recomienda reinicio")
    def reinicio(self):
        print("Reinicio del sistema en progreso......")
        self.enlinea=True
        self.estatus()
    def dagno(self):
        self.enlinea=False

class Space(Armadura):
    def __init__(self, version, arc,orb):
        super().__init__(version, arc)
        """
        Hemos usado el metodo super para llamar al constructor de la clase padre y por ende los atributos que tambien estaban en 
        este metodo
        """
        self.orbita=orb

    def estatus(self):#Hemos sobreescrito el metodo estatus
        super().estatus()#Usamos super para llamar el metodo estatus original
        if(self.enlinea):
            print("La armadura esta en: ",self.orbita)
        else:
            pass