class vector():
    def __init__(self,a1,a2):
        self.u1=a1
        self.u2=a2
    def suma(self,v1,v2):
        self.u1=v1.u1+v2.u1
        self.u2=v1.u2+v2.u2
    def producto(self,v1,v2):
        p=(v1.u1)*(v2.u1)+(v1.u2)*(v2.u2)
        return p
    
class escalar():
    def __init__(self,x):
        self.n=x
    def producto(self,v1,v2):
        p=v1*v2
        return p