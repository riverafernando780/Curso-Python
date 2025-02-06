lista=["napolitana","natasha","wolfita","gatolaza"] #Esta es la sintaxis de una lista
#Si queremos imprimir toda la lista podemos tener podemos usar print
print(lista[:])#Esta sintaxis permite imprimir(usar) toda la lista
print(lista)#Analogamente esta sintaxis tambien
print(lista[1])#Esto nos devuelve el segundo elemento pues al igual que los demas lenguajes las listas se numeran desde cero
print(lista[-1])#A diferencia de los demas lenguajes, este admite indices negativos, que es dar la vuelta en el otro sentido
print(lista[-4])#En este caso napolitana es el lugar 4 de derecha a izquierda

#Las porciones de lista son segmentos o estractos de lista

print(lista[1:3]) #El primer numero "1" denota el lugar de inicio de nuestra porcion, "3" denota el indice hasta el que se va
#                  imprimir excluyendo el ultimo "3"
# La impresion es ["natasha","wolfita"]
# Abreviciones
print(lista[:3]) #Tomamos los primeros "n=3" elementos
print(lista[1:]) #Tomamos del elemento con lugar "1" al final

#La lista puede ser extendida ya que a diferencia de otros lenguajes esta es variable

lista.append("murciegolaz") # Añade un elemento a la lista al final, este es de indice 4 y la lista a cambiado
print("Cambio de lista:")
print(lista[:])
lista.insert(0,"mis gatas y gatos:,3") #Este metodo inserta cosas en el indice correspondiente desplazando lo que había hacia la derecha
print("--------------------------------------------------------------------------------------------------------------------------------")
print(lista[:])
lista.extend(["gatolaz","sisifo","natasha","napolitana"])# Esta instruccion extienda la lista "concatenando" con la nueva lista a la 
#                                                          derecha
print("--------------------------------------------------------------------------------------------------------------------------------")
print(lista[:])
print(lista.index("murciegolaz"))#Devuelve el indice de murciegolaz
# Si "murciegolaz" o el elemento se repitiera, devuelve el indice donde se repita
# Un operador util es "in", nos permite determinar si algo esta en(in) un objeto, en este caso lista
print("natasha" in lista) # Ya que esa especifica cadena de caracteres se encuentra en nuestra lista obtendremos un True
print("gatasha" in lista) #En este caso tendremos un false pues la cadena de caracteres especifica de gatasha no se encuentra en la lista
# Otra cosa de importancia es precisamente que las listas en python pueden albergar varios tipos de caracteres
l=["caracteres",5,True,3.141592] # Una lista con varios tipos de caracteres
print("--------------------------------------------------------------------------------------------------------------------------------")
print(l[:])
l.remove("caracteres") #Note que esto elimina "caracteres de nuestra lista l"
print(l[:]) # La lista se imprime sin "caracteres"
l.remove(True)# Aquí eliminamos true
print(l[:])
l.pop() # Esto elimina el ultimo lugar de la lista
print(l[:])

#Finalmente podemos usar el operador suma "+" como concatenador y el multiplicacion "*" como repetidor
listaT=lista+l #Aquí hemos concatenado las listas
print("La concatenación de listas es:")
print(listaT[:])
listaT=listaT+l*4 # Aquí hemos repetido la lista 
print(listaT[:])