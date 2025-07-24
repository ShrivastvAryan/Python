class Person:
    # name="Aryan"
    # occ='Developer'

    def __init__(self,n,o): #these are the constructors
        print('Hey Im a person')
        self.name=n
        self.occ=o

    def info(self):
        print(f'{self.name} is a {self.occ}')

a=Person('Aryan','Developer')
b=Person('Divya','HR')
b.info()

# a=Person()
# print(a.name)
a.info()