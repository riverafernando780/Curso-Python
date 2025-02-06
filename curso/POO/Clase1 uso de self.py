class Pelicula():#Esta es la sintaxis para definir una clase
    formato="video"#Estas son las propiedades de nuestra clase
    streaming=False
    genero="Desconocido"
    
    def define_genero(self):#Estos son los metodos, ya que modificaran las propiedades de los objetos de esta clase, se indica self 
#                           como parametro, para pasar al objeto mismo
        self.genero=input("Ingrese el genero de la pelicula: ")#self nos permitirta acceder a las propiedades del objeto mismo
    def subir_streaming(self):
        self.streaming=True
    def esta_streaming(self):
        if self.streaming:
            print("La pelicula esta en streaming")
        else:
            print("La pelicula no esta en streaming")

Pelicula1=Pelicula()#Instanciamos una clase, es decir hemos creado un objeto de clase pelicula
print("El formato de mi pelicula es: ",Pelicula1.formato)#Se esta accediendo a las propiedades del objeto creado
Pelicula1.define_genero()#Se utiliza el define_genero del objeto, que permitira cambiar una de las propiedades del objeto
print("¿La pelicula esta en streaming?",Pelicula1.streaming)
Pelicula1.subir_streaming()
print("¿La pelicula esta en streaming?",Pelicula1.streaming)