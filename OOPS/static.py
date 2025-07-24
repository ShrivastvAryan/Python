class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b
    
a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)


#static methods are independent they can be called anywhere
# class ke andar method banane ke lie jaroori ni self option humesha pass krna hai