#Crearemos algunas funciones que no requieren parametros y no devuelven nada
def funcion1():
    n1=10
    n2=11
    n=n1+n2
    print("La suma de n1+n2=")
    print(n)
funcion1() #Hemos llamado a la funcion
#Definiremos una funcion con parametros 
def f2(x):
    if x%1==0:
        print("El numero es entero")
    else:
        print("El numero no es entero")
y=31.1
f2(y) #El caso else
f2(11) #El caso if

def f3(p1,p2):
    p=p1+p2
    return p
u=f3(1,-1)
print(u) #Tenemos un cero