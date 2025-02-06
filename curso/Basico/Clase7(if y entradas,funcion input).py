print("Este programa compara 2 numeros y dice cual es mayor y cual es menor(Prototipo)")
def compara(n1,n2):
    r="El primer numero es mayor"
    if n1<n2:#Despues del if va una condición que devuelva un valor booleano, despues de eso se escriben ":"
        r="El primer numero es menor"#Note que la sentencias del if llevan una identación
    return r
n1=int(input("Ingrese el primer número: "))#El uso de la función input() permite pasar parametros, sin embargo esta siempre devuelve una 
#                                          cadena por lo que es necesario el uso de la función int(), que convierte cadenas o valores 
#                                          flotantes a su parte entera
n2=int(input("Ingrese el segundo número: "))
print(compara(n1,n2))