class ParentClass:
    def parent_method(self):
        print('this is parent mehtod')

class ChildClass(ParentClass):
    def parent_method(self):
        print('Aryan')
        super().parent_method()
    def child_method(self):
        print('this is the child method')
        super().parent_method()

child_object=ChildClass()
child_object.child_method()
child_object.parent_method()