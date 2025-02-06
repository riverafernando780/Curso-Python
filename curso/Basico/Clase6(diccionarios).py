D1={"natasha":"gata","murciegolaz":"gato","gatolaza":"gata"}#El termino antes de los dos puntos es la clave/indice
print(D1)
print(D1["murciegolaz"])
D1["napolitana"]="gata"#Ya que la clave/indice napolitana no existe, esta instrucción crea la clave "napolitana" y agrega el valor gata
D1["Brownie"]="perro"
print(D1)
D1["Brownie"]="perro salchicha gordo balchichaXD" # En este caso dado que la clave Brownie ya existe, no se puede agregar o repetir, así 
#                                                 que se reescribe
print(D1["Brownie"])
del D1["Brownie"]# Esta instrucción elimina la clave "Brownie" junto con su contenido
print(D1)
#Tanto listas como tuplas pueden ser utilizadas para agregar claves a un diccionario
t1=(1,2,3)
D2={t1[0]:"Primer lugar",t1[1]:"Segundo lugar",t1[2]:"Tercer lugar"}
print(D2)
#Es posible agregar una tupla, lista o un diccionario como entrada de un diccionario
l1=list(t1)# Convertimos la tupla en lista
D3={"naturales":l1,"racionales":(5.31,31.3333,2.71)}#Note que agregamos números como listas y tuplas
print(D3["racionales"])
D={"diccionario":D3,"lista":l1,"tupla":t1}#Tambien es posible asignar diccionarios
print(D)
print("-------------------------------------------------------------------------------------------------------------------------------")
print(D.keys())#Este metodo permite obtener las claves de nuestros diccionarios
print(D.values())# Este metodo obtiene los valores del diccionario y no las claves
print(len(D))# Delvuelve la longitud del diccionario