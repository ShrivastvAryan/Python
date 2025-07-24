class Employee:
    companyName='Apple' # class variable
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02 # instance variables because they can be different for everyone
    
    def showDetails(self):
        print(f'the name of the employee is {self.name} and raise amount is {self.raise_amount}')

emp1=Employee('Aryan')
emp1.raise_amount=0.3
#if I do this 
emp1.companyName='Apple India' #ye instance variable create ho jaeyga
#pehle prgram instance variable dhuddnhta hai then class variable pe jata hai tab ni milta
emp1.showDetails() 
emp2=Employee('Rohan')
emp2.showDetails()

# Employee.showDetails(emp1) this is also same as above line
#Instance variables are those which are associated with instances not with the class
#Class variable mtlb u knwo puri class ke same hoga wo use