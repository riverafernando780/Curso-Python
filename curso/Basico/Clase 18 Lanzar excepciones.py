def control_edad():
    a=int(input("Ingresa tu edad: "))
    if a<0 or a>=100:
        raise ValueError ("No es una edad valida")#Con esta instrucción se lanza una excepción es necesario indicarle al 
#                     interprete de python que excepcion se va lanzar, puede ser cualquiera mientras exista en las excepciones de python
#                     otra bondad es que se puede agregar un mensaje personalizado y como una excepcion autentica interrumpira el 
#                     flujo de ejecución, i.e tirara el programa
    if a<18:
        return "Eres menor de edad"
    else:
        return "Felicidades, eres mayor"
try:    
    print(control_edad())
    print("Fin del programa")
except ValueError as EdadRangoIlogico:#Hemos prevenido ese preciso tipo de excepción e incluso hemos personalizado su nombre 
#    con la instrucción as
    print(EdadRangoIlogico)
    print("Programa terminado con errores")