def G_nombres(*palbras):#El asterisco define que esta función recibira una cantidad indeterminada de parametros en forma de tupla
    for i in palbras:
        yield from i#Esta instrucción establece que el generador devolvera los subelementos de los elementos generados

nombres=[]
agregar=True
while agregar:
    nombres.append(input("Agregue un nombre:\n"))
    final=input("Desea seguir agregando nombres?(s/n)")
    if final=="n":
        break;
    elif final=="s" or final=="":
        agregar=True
    else:
        print("Instrucción no reconocida, no se agregaran mas nombres")
        break;

nombrest=tuple(nombres)#Se crea una tupla donde se almacenan los nombres(no es algo necesario pues la lista por si sola bastaba)

Nombres=G_nombres(nombrest)#Note que la tupla se pasa como un solo parametro
Nombres2=G_nombres("Michelle","Lisset","Aurora")
while True:
    print(next(Nombres))#Los subelementos que duvuelve el generador es cada uno de los nombres que se ingreso, pues el elementos es 
#                        UNA unica tupla
    b=input("Presione enter para imprimir mas nombres")
    if b!="":
        break;
while True:
    print(next(Nombres2))#Los sub-elementos que devuelve el generador son caracter a caracter, de cada nombre pues los elementos 
#                         originales son cada nombre: ("Michelle","Lisset","Aurora")
    b=input("Presione enter para imprimir mas nombres")
    if b!="":
        break;