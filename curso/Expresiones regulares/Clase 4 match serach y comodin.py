import re
va1="Fernando Rivera"
va2="Angel García"
va3="Pedro Ramirez"
va4="Casa"
va5="Pasa"
va6="454udhiuewfhiuerhfiuef iqfhiuewfpqosdkl"
if re.match("Fernando",va1):
    """
    Match buscara el patron al principio del string que le pasemos, cuenta con 2 parametros el primero el patron de busqueda y el 
    segundo el string donde se busca
    """
    print("Encontrado1")
else:
    print("No encontrado1")
if re.match("angel",va2,re.IGNORECASE):
    """
    Se puede agregar un tercer patron como "flag", en este caso re.IGNORECASE que no distingue entre mayusculas y minusculas
    """
    print("Encontrado2")
else:
    print("Error en busqueda2")
if re.match("Ramirez",va3):
    print("Encontrado3")
else:
    print("No3")
    """
    Aquí se despliega el no porque a pesar de que el patron de busqueda si esta en la cadena, este patrón no se encuentra al inicio
    """
if re.match(".asa",va4) and re.match(".asa",va5):
    """El metacaracter "." nos sirve para variar dejar variable un caracter, este patrón engloba todas las coincidencias del 
    tipo .asa donde el "." es cualquier caracter como Casa o Pasa"""
    print("Encontrado por metaracter '.'")
if re.match("\d",va6):
    """EL patron \d indica digitos, cualesquiera digitos, por lo que al combinarlo con match son todas las cadenas que inician 
    con digitos"""
    print("Digitos encontrados")
if re.search("iqf",va6):#Search buscara en todo el string como se explica en la clase 1
    print("String encontrado")