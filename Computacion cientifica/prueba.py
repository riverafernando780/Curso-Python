from iapws import IAPWS97
a=IAPWS97(P=7,x=1)
print(a.h,"\n",a.T)