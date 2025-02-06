import re
lista=["Fernando Angel Rivera Garcia","Hector Miguel Rea Garcia","Jesus Alatorre Garcia"]
ini=0
fin=0
print("Buscando".center(60,"-"))
for elemento in lista:
    if re.findall("[r-z]",elemento):
        """
        Con esta instrucción se le dice al interprete que busque todos los strings que tienen caracteres que van de la 
        letra "r" hsta la "z"
        """
        ini=ini+1
        print(elemento)
print("Nueva busqueda".center(60,"*"))
for elemento in lista:
    if re.findall("[v-z]",elemento):
        ini=ini+1
        print(elemento)
print("Nueva busqueda".center(60,"_"))
for elemento in lista:
    if re.findall("^[A-I]",elemento):#Aquí se esta buscando strings que tengan al inicio un caracter del "A" al "I" (uso metacaracter ^)
        ini=ini+1
        print(elemento)

lista=['Se1', 'Ma1', 'Se1', 'Ba1', 'Ma2', 'Ba1', 'Ma3', 'Va1', 'Va2', 'Ma4', 'AaA', 'Ma5:', 'Ma6:',"MaA","MaB","MaC"]

print("Nueva busqueda".center(60,"*"))
for elemento in lista:
    if re.findall("Ma[1-2]",elemento):
        ini=ini+1
        print(elemento)
    if re.findall("Ma[^1-2]",elemento):
        """
        Cuando se pone ^ dentro se tomara el intervalo negado, es decir todos los que no se encuentran en ese intervalo
        """
        print("--",elemento,"--")
    if re.findall("Ma[1-2A-C]",elemento):#Aquí se buscan dos intervalos un númerico y un alfabetico
        print("**",elemento,"**")