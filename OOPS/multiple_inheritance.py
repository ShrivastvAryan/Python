class Employee:
    def __init__(self,name):
        self.name = name

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print("Dancing:", self.dance)

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

#this is how multiple inheritance works, in which more than one class is inherited
#DancerEmployee inherits from both Employee and Dancer       


o=DancerEmployee("Salsa", "Alice")
print(o.name)
print(o.dance )
o.show()
print(DancerEmployee.mro())

#mro tells kon kon kaha kaha kis order mai dhundha jayega