class Animal():
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, "Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark")

class GoldenRe(Dog):
    def __init__(self, color):
        Dog.__init__(self,name='Dog', breed='Golden Re')
        self.color = color

#this is multilevel inheritance , GoldenRe inherits from Dog

class Cat(Animal):
    def __init__(self, name, breed,color):
        Animal.__init__(self,name, "Cat")
        self.breed = breed
        self.color = color

    def make_sound(self):
        print(f'the color of the cat is {self.color}')
        print("Meow")

#This is single inheritance, Dog inherits from Animal
#Creating instances of Dog and Animal to demonstrate functionality

d=Dog('Dog','Golden Retriever')
d.make_sound() 

a=Animal('Lion','Panthera leo')
a.make_sound()

c=Cat('Kitty','Siamese','White')
c.make_sound()

g=GoldenRe('Golden')
print(g.color)

