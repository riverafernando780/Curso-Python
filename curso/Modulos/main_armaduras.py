from modulo_armaduras import *
GodKiller=Space("model 3(Godkiller)",True,"orbita")
GodKiller.estatus()
print(isinstance(GodKiller,Space))
"""
Usamos el metodo isinstance para corroborar que el objeto Godkiller es de clase "Space" o "Armadura", esto devuelve true o false
"""
print(isinstance(GodKiller,Armadura))