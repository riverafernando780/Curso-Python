a="Este programa capitaliza nombres"
print(a.center(len(a)+20,"-"))
"""
Recordemos que en python todos son objetos, hasta los string, usamos el metodo center para generar una nueva cadena de caracteres 
centrada, el primer parametro del metodo nos pide la longitud de la nueva cadena "un valor entero", utilizamos la función len, para 
asegurar la longitud de la cadena original y sumamos 20 espacios mas, el otro parametro es el string que se ocupara para rellenar 
los espacios con los que se centra la cadena, dando 10 y 10, de la siguiente forma
----------cadena----------
"""
retorno=False
while(retorno==False):
    nombre=input("Ingrese un nombre valido:\n")
    guarda_nombre=nombre.split()
    """
    Este metodo nos permite extraer las cadenas separadas por un espacio y guardarlas en una lista, como:
    cadena ingresada->split
    Resultado:
    [cadena,ingresada]
    """
    nombre=""
    for i in guarda_nombre:
        retorno=i.isalpha()
        """
        Este metodo regresa un valor booleano verifica que el string sea alfabetico, es decir solo caracteres de tipo A-Z y a-z 
        sin incluir espacios, si detecta un espacio o cualquier caracter fuera de este conjunto devuelve FALSE
        """
        if(retorno==False):
            break;
        nombre=nombre+" "+i.capitalize()#Este metodo capitaliza el string en cuestión, hola MUNDO->Hola mundo
"""
Note que usando el metodo title para estring podiamos obtener resultados como hola MUNDO->Hola Mundo, sin embargo, hacer el 
programa sin usar este metodo resulta mas enrriquecedor
"""

print("El nombre capitalizado es:\n",nombre.center(len(nombre)+20,"-"))