from modulo_areas_perimetros import rectangulo
"""
Esta forma permite importar una parte especifica del modulo, de esta manera no tenemos que invocar el modulo completo a la hora 
de usar la función rectangulo
"""
a="Calcularemos el area y perimetro de un rectangulo"
print(a.center(len(a)+20,"-"))
rectangulo()
#Note que es imposible usar otra parte del modulo, pues solo podemos cargar la función rectangulo(esto economiza memoria y recursos)