#classes are way to define custom datatypes

class Employee:
    company='Apple'
    def show(self):
        print(f'The name of company is {self.company}')

    @classmethod
    def changeCompany(cls,newCompany): #this is class method
        # cls here works as class
        cls.company=newCompany

e1=Employee()
e1.name="Aryan"
e1.show()
e1.changeCompany('Maruti')
e1.show()