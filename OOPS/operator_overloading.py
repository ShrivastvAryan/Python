class Vector_class():
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return(f'{self.i}i+{self.j}j+{self.k}k')
    
    def __add__(self,x):
        return Vector_class(self.i+x.i,self.j+x.j,self.k+x.k)


v1=Vector_class(3,5,6)
v2=Vector_class(1,2,3)
v = v1 + v2
print(v)
print(type(v))

# Vector() is not a built int type in python