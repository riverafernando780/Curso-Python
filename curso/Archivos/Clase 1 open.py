from io import open
"""
La biblioteca io es la que nos permitira leer y escribir en archivos, ya que en este caso solo abriremos archivos para leer o darles 
información solo necesitamos el modulo open
"""
archivo_texto=open("archivo de prueba.txt","w")
"""
Se crea un objeto para manipular el archivo, con dos parametros, el primer parametro escribe el nombre del archivo que vamos a 
trabajar IMPORTANTE, SEGUN LA CARPETA DE TRAVBAJO QUE SELECCIONEMOS VSCODE EN CONJUNTO CON PYTHON BUSCARAN EN LA RAIZ DE ESA CARPETA 
DE TRABAJO PARA HALLAR MANIPULAR O CREAR EL ARCHIVO.
El metodo de escritura "w", nos peermite escribir el contenido del archivo(esto elimina cualquier contenido y reescribe el nuevo)
Nota:En este modo si el archivo no existe se va crear
"""
escritura=input("Ingrese lo que desea escribir en el archivo:\n")
archivo_texto.write(escritura)
"""
Ya que python a cargado el archivo a travez de un objeto con la función open, el modo escritura podemos usar el metodo "write" y 
en parametro pasarle el string nuevo que queramos que se escriba en el archivo
IMPORTANTE, el metodo write inserta caracteres y si hay caracteres en el cursor en donde comienza escribir los sobreescribira
"""
archivo_texto.close()#Este metodo cierra el archivo para python, liberando los recursos o memoria que requería para mantenerlos abiertos
archivo_texto=open("archivo de prueba.txt","r")
"""
Este metodo abre el archivo en modo lectura parametro "r", de esta manera python solo puede cargar o extraer la información del archivo, pero 
no modificarla
"""
lectura=archivo_texto.read()
"""
Este metodo permite cargar todo el contenido del archivo en un objeto propio, util para usar esa información o manipularla en el 
programa pero no en el archivo original, este metodo devuelve un String
"""
archivo_texto.close()
print("El contenido del archivo es:\n",lectura)
archivo_texto=open("soy texto.txt","r")
lectura=archivo_texto.readlines()
"""
Este metodo tambien extrae el contenido del archivo pero devuelve una lista donde cada lugar es precisamente una linea del archivo en 
cuestión, util para busqueda de información por lineas o leer formatos especificos en un archivo
"""
archivo_texto.close()
print("Que sucede con las lineas, esto:\n",lectura)
archivo_texto=open("archivo de prueba.txt","a")
"""
El metodo append parametro "a", permite agregar información sin reescribir el archivo, es decir, la información original se conserva 
y se agrega mas despues de esa información
"""
escritura=input("Esto se añadira al archivo:\n")
archivo_texto.write("\n"+escritura)
"""
Para usar el modo append, se puede usar el metodo escritura, note que concatenamos dos string un salto de linea con otro string
"""
archivo_texto.close()
archivo_texto=open("archivo de prueba.txt","r")
lectura=archivo_texto.read()
archivo_texto.close()
print("El contenido modificado del archivo:\n",lectura)