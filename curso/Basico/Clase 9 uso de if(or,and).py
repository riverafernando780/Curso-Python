print("El siguiente programa nos permitira establecer la tricotomia entre una tercia de numeros")

def orden(a,b,c):
    if type(a)==bool or type(b)==bool or type(c)==bool or type(a)==str or type(b)==str or type(c)==str:#Aquí or es el operador booleano 
#                                                                                                       de siempre
        return "Los datos son ilegibles"
    else:
        if a==b or b==c or c==a:
            D={a:"=",b:"=",c:""}
        elif a<b and b<c: #Aquí and es el operador & de siempre
            D={a:"<",b:"<",c:""}
        elif a<b and c<a:
            D={c:"<",a:"<",b:""}
        elif b<a and c<b:
             D={c:"<",b:"<",a:""}
        else:
            D={b:"<",a:"<",c:""}
    return D

#Hay que perfeccionarloXD pero se entiende la idea, esta función es mejor cargarla al idle
