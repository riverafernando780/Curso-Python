#A diferencia de otros lenguajes la estructura del for es muy distinta, aunque su proposito y función es la misma

for i in (1,2,3):#Note que a diferencia del if "in" en for no es reconocida como una instrucción logica, en los ciclos for "in", indica 
#                 el recorrido que el iterador tiene que hacer, en este caso esta recorriendo una tupla de elementos enteros, el 
#                 numero de elementos es 3 por lo que el recorrido le tomara 3 iteraciones, sin embargo otra cosa importante de notar 
#                 es que mientras i recorre la tupla, tambien va adquiriendo esos valores
    print("Este mensaje se repite por: "+str(i)+"-esima vez\n")#Por lo que fue necesario convertirla a string
print("Inicia la construcción de la piramide\n")
for i in ("   1","  111"," 11111","1111111"):#Note que el numero de itaraciones es 4, pues hay cuatro elementos a recorrer
    print(i)
print("\n")
#Otra forma de utilizar el ciclo for es por medio de el tipo range
for i in range(5):#Similar a poner int i=0 i<5 
    print(i)