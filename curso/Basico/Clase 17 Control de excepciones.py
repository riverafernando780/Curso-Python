def duplicar(a):
    return 2*a
error=0
try:#try encapsula la linea de error que ocaciona la excepción, note que tambien se incluye print, aunque la excepción no es 
#    propiamente de la función print, esta carece de error sin la variable "a"
    a=float(input("Ingrese un numero a duplicar: "))#El codigo espera que la cadena de caracteres que se ingrese sea un número real, sin
#                                                    embargo esto puede no suceder por lo que es conveniente controlar ese posible error
    print(duplicar(a))
except ValueError:#Solo hay que asignar el nombre la excepción y poner que hacer en ese caso, esto permite que el codigo siga 
#                  en ejecución.
#                  En general se pueden agregar tantas excepciones como se quiera, poniendo except con la misma identación(como elif)
    print("El dato ingresado no es un número")
    error+=1
finally:#Otra instrucción util es finally, esta va ejecutar un codigo haya excepciones o no
    print("El primer bloque se ha completado")

try:
    print(duplicar(int(input("Ingrese un valor entero a duplicar: "))))
except:#Si no se especifica una excepcion cualquier problema error dentro de try detonara except, es decir que se ejecutara 
#    ante cualquier excepcion/error
    print("Error inesperado")
    error+=1

print(f"El programa ha terminado con ''{error}'' errores")    