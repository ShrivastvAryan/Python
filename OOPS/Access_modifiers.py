class Employee:
    def __init__(self):
        self.name='Aryan'


a=Employee()
print(a.name)

#by default python mai jo bi banate ho public hota hai
# To create private modifier
# By name mangling
#is done by _class__name
# ye python ni kuch deta ye hum marji se vary kr 
# skte hai python bas jaha double underscore lagaoge waha mangling kr dega
#__ laga dia toh direct access ni kr skte
#_ is a naming conevntion