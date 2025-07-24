class Person:
    name='Aryan'
    occupation='Software Developer'
    networth=10000

    def info(self):
        print(f'{self.name} is a {self.occupation}')

#self matlab wo oject jiske lie ye method call kia jaa raha hai

a=Person()
# print(a.name,a.occupation)
# can be mutated by
#a.name='Shubam' --> this will replace the name to Shubham
a.info()