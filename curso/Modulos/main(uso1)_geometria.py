import modulo_areas_perimetros#Esta es la forma mas básica de importar un modulo
a="Calcularemos el area y perimetro de un rectangulo"
print(a.center(len(a)+20,"-"))
modulo_areas_perimetros.rectangulo()
"""
Para usar cualquier función o recurso de un modulo, debe verse al modulo completo como un "objeto", así cada las funciones o 
recursos dentro del modulo son metodos o atributos y se usan como tal
"""
b="Calcularemos el area y perimetro de un circulo"
print(b.center(len(b)+20,"-"))
modulo_areas_perimetros.circulo()