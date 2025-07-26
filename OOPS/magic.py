class Employee:
    name='Aryan'
    def __len__(self,name):
        i=0
        for item in self.name:
            i=i+1
        return i

e=Employee()
print(e.name)

#need to complete