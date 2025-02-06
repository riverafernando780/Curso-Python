class vector():
    def __init__(self,a1,a2):
        self.u1=a1
        self.u2=a2
    def suma(self,v1,v2):
        self.u1=v1.u1+v2.u2
        self.u2=v1.u2+v2.u2
    def producto(self,v1,v2):
        """
        Note que propiamente este metodo no requiere acceder a los atributos del vector self.u1. self.u2 o algun otro atributo, sin embargo 
        el no usar el self generara errores
        """
        p=(v1.u1)*(v2.u1)+(v1.u2)*(v2.u2)
        return p
    
class escalar():
    def __init__(self,x):
        self.n=x
    def producto(self,v1,v2):#Este objeto tambien tiene un metodo producto con los mismos parametros
        p=v1*v2
        return p

def Producto(Vector,v1,v2):
    """
    Esta función recibira tres parametros, se asume que uno de los parametros es un objeto que cuenta con un metodo llamado 
    producto con 2 parametros justo como "vector" y "escalar"
    """
    return Vector.producto(v1,v2)#Note que para cada caso ambos metodos retornan un objeto
print("Este programa ilustra el polimorfismo")
#A continuación se generan dos objetos de tipo escalar y vector
vector1=escalar(0)
vector2=vector(0,0)
opcion=input("Ingrese ''v'' para producto punto\nIngrese ''e'' para producto de escalares(v/e): ")
if(opcion=="v"):
    print("Operacion por vectores")
    a1=float(input("Ingrese la primer entrada del primer vector:\n"))
    a2=float(input("Ingrese la segunda entrada del primer vector:\n"))
    b1=float(input("Ingrese la primer entrada del segundo vector:\n"))
    b2=float(input("Ingrese la segunda entrada del segundo vector:\n"))
    a=vector(a1,a2)
    b=vector(b1,b2)
    print("El producto es punto: ",Producto(vector2,a,b))
    """
    Se usa la función producto aqui se aplica el polimorfismo pues el objeto de la función toma la forma de vector, pues así 
    lo require el codigo
    """
elif(opcion=="e"):
    print("Operacion de escalares")
    e1=float(input("Ingrese el primer escalar:\n"))
    e2=float(input("Ingrese el segundo escalar:\n"))
    print("El producto es: ",Producto(vector1,e1,e2))#Analogamente el objeto toma la forma escalar
else:
    print("Instrucción no reconocida")