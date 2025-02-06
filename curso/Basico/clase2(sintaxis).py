#Verificaremos que es lo que hacen algunos operadores
a=5**2 # Esto es equivalente algebraicamente a 5^2
print(a)
a=5//2 #Este operador nos otorga la parte entera de la division, en este caso 2
print(a)
type(a) # Esta función nos permitira determinar el tipo de dato
print(type(a))
a="ya soy cadena"
print(type(a)) # Aquí el tipo a cambiado
n1=10
n2=n1
if n1==n2:
    print("n1=n2")
else: #aguas con la identacion
    print("no son iguales")
n2=n1+1
if n1==n2:
    print("n1=n2")
else: #aguas con la identacion
    print("no son iguales")