import re#El modulo re nos permite trabajar con expresiones regulares
cadena="Hola soy un textoXD"
print(re.search("Hola",cadena))#Aqui devolvio un objeto
"""
El metodo search pide dos parametros, el String a buscar como primer parametro y como segundo el String donde se buscara, este metodo 
devuelve un objeto si se encuentra el string a buscar o devuelve none(nada) si no lo encuentra
"""
print(re.search("hola",cadena))#Aqui devolvio none
buscador=re.search("Hola",cadena)#Estamos guardando el objeto de la busqueda
print("Start: ",buscador.start(),"\nEnd: ",buscador.end(),"\nspan: ",buscador.span())
"""
El crear un objeto por el metodo search nos permite utilizar otros 4 metodos(start,end,span), el metodo start nos dice a partir de 
que caracter esta nuestra expresión, el metodo end donde termina y el metodo span genera una tupla de dos entradas (start(),end())
"""
cadena2=cadena*2
print(re.findall("soy",cadena2))
"""
Finalmente el metodo findall pide dos parametros, el string a encontrar y el string donde se buscara, este devolvera una lista en 
donde se repetira las veces que se encuentre el string el mismo string buscado
"""