class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showDetails(self):
        print(f'The name of employee {self.id} is {self.name} ')


class Programmer(Employee): #this is inheritance
    def showLanguage(self):
        print('The default language is python')

    
e=Employee('Rohan Das',420)
e.showDetails()
e1=Programmer('Aryan',300)
e1.showLanguage()
e1.showDetails()