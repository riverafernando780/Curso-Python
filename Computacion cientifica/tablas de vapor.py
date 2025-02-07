from iapws import IAPWS97
#Para calcular propiedades en la saturacion se requiere algun parametro, usualmente la presion o la temperatura y la calidad
P1=0.75
X_1=0
agua=IAPWS97(P=P1,x=X_1)
"""
La presión debe ser en MPa y la temperatura en kelvin, dado que la calidad es 0, este objeto puede determinar las propipiedades 
termodinamicas del agua en la saturación en su estado liquido, es decir hf, vf, etc
"""
print("La entalpia del agua saturada a presion:",P1,"MPa es: ",agua.h,"kj/kg")
#Para calcular las propiedades en la región subenfriada se utilizan dos parametros usualmente
agua=IAPWS97(P=7,T=490.15)
print(agua.h)
a=IAPWS97(P=7,x=1)#Importante la calidad va de 0 a 1
print(a.h,"\n",a.T)