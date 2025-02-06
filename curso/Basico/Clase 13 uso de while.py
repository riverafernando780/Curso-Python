Angulos=(0,30,45,60,90,180,270,360)
a=int(input("Escriba alguno de los angulos ''famosos'': "))
if a in Angulos:
    i=False
else:
    i=True
while i==True:#El while es practicamente lo mismo a otras estructuras de otros lenguajes
    a=int(input("Intenta otra vez\nEscriba alguno de los angulos ''famosos'': "))
    if a in Angulos:
        break;#Permite salir de cualquier ciclo while
print(f"Bien hecho: {a}° es un angulo conocido")