from paquete1.modulo_vector import * 
"""
Los paquetes se importan de la misma forma que los modulos y se usa la sintaxis del punto para extraer los modulos necesarios, 
tambien se puede importar solo la parte necesaria del paquete como con rectangulo
"""
from paquete1.subpaquete.areas_perimetros import rectangulo
a="Este programa suma y resta vectores de R^2"
print(a.center(len(a)+20,"-"))

u1=float(input("Ingrese la primer componente:\n"))
u2=float(input("Ingrese la segunda componente:\n"))
u=vector(u1,u2)
print("El vector ingresado es:\n"+"(",u.u1,",",u.u2,")")
print("Ingrese un segundo vector")
b1=float(input("Ingrese la primer componente:\n"))
b2=float(input("Ingrese la segunda componente:\n"))
b=vector(b1,b2)
print("El vector ingresado es:\n"+"(",b.u1,",",b.u2,")")
r=vector(0,0)
print("Sumando vectores:")
r.suma(u,b)
print("La suma es:\n"+"(",r.u1,",",r.u2,")")
print("Supon que cada vector representa un rectangulo, entonces")
print("Para el primer vector: ")
rectangulo(u.u1,u.u2)
print("Para el segundo vector: ")
rectangulo(b.u1,b.u2)
print("Para la suma vector: ")
rectangulo(r.u1,r.u2)