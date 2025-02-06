from setuptools import setup
setup(name="paquete de peliculas"
      ,version="0.1",description="Prueba de paquetes distribuibles"
      ,author="Fernando Rivera",author_email="fercho_212@hotmail.com"
      ,url="no may:c"
      ,packages=["pack","pack"])
"""
La instrucción importante es packages, que se compone de dos parametros, la primera la carpeta general en donde se encuentra 
el paquete, la segunda, la ruta completa, ya que el modulo pelicula se encuentra en "pack" no necesitamos añadir mas rutas
"""