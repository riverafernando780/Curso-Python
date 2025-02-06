class Pelicula_1():#Primera versión de nuestra clase pelicula
    def __init__(self):#Esta es la forma de crear un constructor
        self.__formato="video" """En este caso hemos encapsulado el formato pues una pelicula siempre es de formato video por lo 
        que conviene que en nuestro codigo esta no pueda ser modificada"""
        self.streaming=False#Note que las caracteristicas estan detro del constructor
        self.genero="Desconocido"
        self.nombre=""
    
    def define_pelicula(self,nombre):
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
                  ,"y de formato",self.__formato)#Siempre que se referencia la caracteristica formato debera hacerse con "__" 
#                                                 pues esta esta encapsulada
        elif a=="n":
            print("No se motrara el estado")
        else:
            print("funcion no reconocida")

movie=Pelicula_1()#Aqui se ha creado un objeto pelicula con el constructor y este tiene la propiedad formato encapsulada
movie.fichaT()