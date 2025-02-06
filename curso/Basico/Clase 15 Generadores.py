print("Este codigo establece el uso de generadores")
def f_tablas(num,lim):#Esta es una función cualquiera
    tablas=[]
    for i in range(1,lim+1,1):
        tablas.append(num*i)
    return tablas

a=int(input("Ingrese el numero del que desea sacar la tabla de multiplicar: "))
b=int(input("Ingrese el limite hasta el cual desea obtener la tabla de multiplicar: "))
print(f"La tabla de multiplicar es: {f_tablas(a,b)}")
#Ahora veamos como se haría esto con un generador
def generador_tablas(num,lim):
    
    for i in range(1,lim+1,1):#Ya que la naturaleza de un generador es un objeto iterable este se crea a partir de un bucle
        yield num*i#Esto es muy importante, ya que estamos creando un objeto iterable, que se va construyendo cada vez que se llama al generador

print("La tabla de multiplicar usando generadores")

for i in generador_tablas(a,b):
    print(i) #Note que no estamos imprimiendo el generador, si no lo que devuelve el generador en cada iteración y eso es importante
#             un generador NO SE PUEDE IMPRIMIR

def g_potencias2(n):#Este es un generador de la suseción n^k
    k=1
    while True:#Nuevamente el generador se crea a partir de un bucle, esta suseción es infinita por lo que el ciclo while se mantiene 
#               activo "siempre", mas sin embargo el estado de stanby del generador previene el uso excesivo de memoria y procesador
        yield n**k
        k+=1
paso=""
orden=1
base=int(input("Ingrese la base de la que desea obtener una suseción p^k: "))
susecion_base=g_potencias2(base)#Es importante utilizar una variable para fijar el generador en ella, ya que el uso del generador solo
#                               lo reiniciara constantemente
while paso=="":
    print(f"El termino {orden}-enesimo de la suseción {base}^k es: {next(susecion_base)}")#Una forma clave para usar el generador, 
#                      es por medio de la función next(variable), esta extrae el valor de nuestro generador en el momento que es llamada
    orden+=1
    paso=input("Presione enter para continuar:")