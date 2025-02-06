class Pelicula():
    formato="video"
    streaming=False
    genero="Desconocido"
    nombre=""
    
    def define_pelicula(self,nombre):#Note que a los metodos tambien se le pueden agregar parametros y usarlos
        self.genero=input("Ingrese el genero de la pelicula: ")
        self.nombre=nombre
    def streaming(self,enlinea):
        self.streaming=enlinea
        if self.streaming:
            print("La pelicula esta en streaming")
        else:
            print("La pelicula no esta en streaming")
    def fichaT(self):
        a=input("Desea imprimir la ficha técina(s/n): ")
        if a=="s":
            print("La pelicula ''",self.nombre,"'' de genero ",self.genero
                  ,"y de formato",self.formato)
        elif a=="n":
            print("No se motrara el estado")
        else:
            print("funcion no reconocida")

Pelicula1=Pelicula()
Pelicula1.define_pelicula("La toalla del mojadoXD")#Aqui pasamos como parametro un string, utilizado para definir nombre a nuestra pelicula
Pelicula1.streaming(False)
Pelicula1.fichaT()