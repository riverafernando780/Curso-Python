print("Este programa escribe las tablas de multiplicar")
tabla=int(input("Ingrese el numero natural del cual desea crear la tabla de multiplicar: "))
print(f"Se creara la tabla del: {tabla}")#Cuando f se coloca como parametro de la funcion print este aceptara variables de todo tipo 
#                                         entre "{}", util para evitar la transformación de datos a caracteres y la concatenación
for i in range(1,11,1):
    r=i*tabla
    print(f"{tabla}X{i}={r}")
print("El programa ha terminado")
#Hablemos mas de las 3 formas de uso de range
#range(n), define un rango de n lugares con un paso de 1
#range(n1,n2), define un rango de n1 hasta n2
#range(n1,n2,step), define un rango de n1 hasta n2 con un paso "step"