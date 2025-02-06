print("Menciona un album de estudio de la banda Gorillaz")

album=input("Ingresa el album a continuación:\n").capitalize()

if album in ("Gorillaz","Demon days","Plastic beach","The fall","Humanz","The now now","Song machine","Cracker island"):
    print("Eres buen fan, efectivamente ´´"+album+"´´ es un ambum de estudio Gorillaz")
else:
    print("Ese album no es un album de estudio de Gorillaz")