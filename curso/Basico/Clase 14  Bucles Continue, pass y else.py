print("Este programa identifica el número de caracteres no blancos de un string")


def funcion_de_espacios():
    cadena=input("Ingrese un texto a analizar:\n")
    contador=0
    for i in cadena:
        if i==" ":
            continue#Esta instrucción le dice a python que continue a la siguiente iteración de ciclo, por lo que el contador no se ve 
    #                incrementado en espacios en blanco
        contador+=1
    print("La cadena de caracteres ingresada fue:\n"+cadena)
    print(f"Esta cadena se compone de ''{len(cadena)}'' caracteres, sin contar los espacios en blanco ''{contador}''")
    print(f"Es decir {len(cadena)-contador} espacios en blanco")

def funcion_vacia():
    pass #En este caso no sabemos que hacer con la función por el momento, sin embargo dejarla vacía marcaria un error por el 
#         interprete de python, por lo que colocar pass nos ayuda a no quebrantar las reglas y dejarla vacia para usarla despues

def basic_function():
    cadena=input("Ingrese un texto a analizar:\n")
    for i in cadena:
        if i==" ":
            indicador=True
            break;
    else:# Else es una condición que se ejectuta siempre que el bucle termine, en este caso cuando i barra el ultimo caracter y ejecute 
#          todo lo de dentro se ejecuta la parte else del bucle, si el ciclo se rompe o termina antes, la instrucción else 
#          jamas se va ejecutar
        indicador=False
    print(f"La cadena de caracteres:\n{cadena}\ncuenta con espacios en blanco->{indicador}")

o=input("1: Si desea un analisis completo\n2: Analisis Básico\n")
if o=="1":
    funcion_de_espacios()
elif o=="2":
    basic_function()