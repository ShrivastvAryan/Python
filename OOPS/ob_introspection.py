x=[1,2,3]

#print(dir(x)) tell which methods are theree in list 
#same works for tuples 
#return all the attributes

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1

p=Person('Aryan',30)
print(p.__dict__) # give the data in form of dictionary

print(help(Person)) # use to get help documentation for objects
