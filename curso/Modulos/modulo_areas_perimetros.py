#Este modulo puede calcular algunas areas y perimetros
import math

def rectangulo():
    l=float(input("Ingrese el largo: "))
    a=float((input("Ingrese el ancho: ")))
    p=2*l+2*a
    A=l*a
    print("El rectangulo de ancho: ",a,"u y largo: ",l,"u"
          +"\nTiene un perimetro de: ",p,"u\nTiene un Area de: ",A,"u^2")
    
def circulo():
    r=float(input("Ingrese el radio: "))
    p=2*(math.pi)*r
    A=(math.pi)*(r**2)
    print("El circulo de radio: ",r,"u"
          +"\nTiene un perimetro de: ",p,"u\nTiene un Area de: ",A,"u^2")