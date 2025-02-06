print("Este programa perfecciona el programa anterior")
print("---------------------------------------------------------------------------------------------------------------------------------")
print("Programa para comparar números")
n1=int(input("Ingrese el primer número:\n"))
n2=int(input("Ingrese el segundo número:\n"))
if n1<n2:
    print(str(n1)+"<"+str(n2))#Note que print solo puede trabajar con cadenas y como en JAVA, estas se pueden concatenar ya que n1 y n2
#                              originalmente son valores enteros utilizamos la función str() para convertir esos valores a string y 
#                              usamos "+" para concatenar varios string
else:#Note que para agregar else este requiere estar a la misma sangría que el if original y corresponde al if mas cercano
    print(str(n2)+"<="+str(n1))

print("Perfeccionando el codigo:")
print("---------------------------------------------------------------------------------------------------------------------------------")
if n1<n2:
    print(str(n1)+"<"+str(n2))
elif n1==n2:#Otra instrucción importante es elif, que sirve para agregar varios if, es una alternativa de if's anidados, este se coloca
#            a la misma altura que el if anterior y si no se cumple entonces y tampoco el if anterior, se ejectua el else
    print(str(n1)+"="+str(n2))
else:# Note que else conserva su estructura y la misma identación
    print(str(n2)+"<"+str(n1))
#Algo importante esque se pueden usar tantos elif como sea necesario