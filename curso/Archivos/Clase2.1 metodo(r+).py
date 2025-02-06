from io import open
cursor=open("clase2.1.txt","r+")
"""
Un modo util para la creación de nuestros objetos que manipulan archivos es el modo lectura y escritura. 
Se logra con el parametro "r+"
"""
print("Leemos el contenido del archivo\n",cursor.read())
cursor.seek(0)
a=input("Ingrese la información que desea agregar al archivo: ")
cursor.write(a)#Ademas de leer nos permite escribir
cursor.seek(0)
print("Se agrego exitosamente, el archivo actualizado es:\n",cursor.read())
cursor.seek(0)
lineas_texto=cursor.readlines()
cursor.writelines(lineas_texto)
"""
Este metodo requiere como parametro una lista y agregara cada lugar de la lista como una linea del cursor, es 
importante que sobreescribe y depende de la posición del cursor así como el metodo write()
"""
t="Procedemos a duplicar el archivo"
cursor.seek(0)
print(t.center(len(t)+36,"-"),"\n",cursor.read())
cursor.close()