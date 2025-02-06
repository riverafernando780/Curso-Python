print("Este programa valida estructuras de correo electronico")
c=input("Ingrese un correo electronico:\n")
c2=c.lower()#se crea una nueva cadena de caracteres convirtiendo el "correo" original en su versión de minusculas
contador=0#Este contador nos permitira contar "@" y "#"
especial=("|","#","$","%","&","/","(",")","=","'","?","¡","!")#Esta tupla es una pequeña base de datos de caracteres prohibidos 
#                                                              en correos electronicos
lista_correo=[]#Aprovechahdo que las listas son dinamicas, se crea una lista vacia en donde se guardara cada caracter del correo
verificador=True#Esta variable nos ayudara a determinar si nuestro correo es correcto
j=0#Este iterador lleva el control de la longitud de lista_correo
if c2==c:#Nos preguntamos si nuestro correo contiene una mayuscula
    for i in c:#Nuestro ciclo for recorre toda la cadena de caracteres que compone al correo ingresado
        lista_correo.append(i)#Cada elemento es agregado a la lista_correo, caracter a caracter
        j=j+1#El iterador j se incrementa
        if i=="@" or i==".":
            contador=contador+1#Si se detectan "@" o "." el contador incrementa
        elif i in especial:# Se verifica caracter por caracter del correo ingresado que este no sea especial
            verificador=False
    if lista_correo[0]=="@" or lista_correo[j-1]=="." or contador!=2 or lista_correo[0]=="." or lista_correo[j-1]=="@":#Se consideran
#                                                                               las posiciones de "@" y "." sean cuando menos logicas
        verificador=False
else:#Ya que si el correo tiene una mayuscula no es valido
    verificador=False

if verificador:
    print("El correo: "+c+" es autentico",end="\nFin del programa")#Note que se puede elegir la forma en la que termina el print, por 
#                                                                   defecto "\n"
else:
    print("El correo: "+c+" es apocrifo",end="\nFin del programa")