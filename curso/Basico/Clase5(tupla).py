t1=("str",22,33,44,55.5,True) # Las tuplas tambien pueden recibir elementos de varios tipos
print(t1[3:]) #La sintaxis con corchetes tambien es valida, al igual con la lista o simplemente tomar por completo todo el elemento
print(t1)
l1=list(t1)*2 #La función list convierte una tupla en lista, notese la diferencia en la forma de impresion
print(l1)
t2=tuple(l1) #Esto convierte la lista en una tupla
print(55.5 in t2) #Tambien se puede usar el operador in
print(t2.count(22))# este metodo verifica si el parametro existe en la tupla y si si lo cuenta(las veces que se repite)
print(len(t2))# Devuelve la longitud de la tupla
t3=("Soy una tupla unitaria",)# Esto define una tupla de una sola entrada
print(len(t3))
#Empaquetado de tuplas
fer="fernando",21,"Febrero",1999 #Esto crea una tupla, note que los "()" en realidad no son necesarios, sin embargo a esta practica
#                                  se le conoce como empaquetado pues da la idea de asignar varios valores a una sola entidad(tupla)
#                                  muy importante mencionar que es LO MISMO, solo es una idea
print(fer)
#Desempaquetado de tupla
nombre,dia,mes,agno=fer# Aquí el proceso inverso, hemos dado varias variables separadas por comas, y al asignarles la tupla estas se 
#                       dividen el contenido de forma equitativa
print(mes)