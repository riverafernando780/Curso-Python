from io import open
cursor=open("Clase 2.txt","r")
print(cursor.read())
"""
Al usar por primera vez el metodo read esta utiliza un cursor y hace la lectura desde el mismo, ya que es la primera vez que se 
utiliza en el codigo para este archivo, leera desde el inicio hasta el final, sin embargo el cursor se quedara en la posición final
"""
print("Volvemos a imprimir:\n",cursor.read(),"\nNote que no hay nada escrito en la linea anterior"
      +" esto se debe a que el cursor despues de la primera lectura se ha colocado al final del archivo y ahí permanece")
cursor.seek(0)
"""
El metodo seek nos permite colocar el cursor de nuestro objeto de manipulación de archivos en donde queramos, la 
posición "0", es al principio del archivo
"""
medidor=cursor.read()
print("La longitud de caracteres del archivo es: ",len(medidor))
posicion=int(input("Ingrese el valor en donde quiere colocar el puntero entre 0 y "+str(len(medidor))+":\n"))
cursor.seek(posicion)
print("El puntero se ha posicionado en la posición: ",posicion,"\nEl mensaje es:\n",cursor.read())
cursor.seek(0)
print("La parte que no se imprimio es: \n",cursor.read(posicion))
"""
Usar un parametro para el metodo read hace referencia al tamaño del string que devolvera para la lectura, otra forma de 
verlo, desde la posición del cursor leera el numero de caracteres indicado en el parametro
"""
cursor.seek(0)
medidor=cursor.readlines()
print("Las lineas de texto del archivo en cuestión son: ",len(medidor))
posicion=int(input("Ingrese la linea de donde desea leer: "))
cursor.seek(0)
for i in range(posicion-1):
    cursor.readline()
    """
    Otro metodo interesante es readline, que leera la linea de donde el cursor se encuentra y la dejara al final de esa linea
    """
print("La linea seleccionada es: ",posicion,"\nLa linea en cuestión es:\n",cursor.readline())
cursor.close()