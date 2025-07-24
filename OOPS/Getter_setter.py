class MyClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f'value is {self._value}')
    @property
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10

    
    
obj=MyClass(10)
obj.ten_value=67
print(obj._value)
obj.show()

#getters are methods in python that are used to access values of an object propoerties
#@property is the decorator
#