import re
lista=["Fernando Angel Rivera Garcia","Hector Miguel Rea Garcia","Jesus Alatorre Garcia"]
ini=0
fin=0
for elemento in lista:
    if re.findall("^Fernando",elemento):#Un metacaracter especial es el "^", encuentra coincidencias al inicio
        ini=ini+1
        print(elemento)
print("Se encontraron ",ini," coincidencias")
print("Busqueda dos en progreso")
for elemento in lista:
    if re.findall("Garcia$",elemento):#Metacaracter "$", encuentra coindicencias al final
        fin=fin+1
        print(elemento)
print("Se encontraron ",fin," coincidencias")
lista=["Gatitos","Perritos","Gatitas","Perritas","ocasión","ocasion"]
patron=0
for elemento in lista:
    if re.findall("it[oa]s",elemento):#Busca patrones, en este caso frases "itos" e "itas", ambos patrones
        patron=patron+1
        print("Animal chiquito: ",elemento)
    elif re.findall("ocasi[oó]n",elemento):
        patron=patron+1
        print("Coincidencias encontradas: ",elemento)
print("Se encontraron ",patron," coincidencias")