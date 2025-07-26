class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)  # x and y both = radius

    def area(self):
        return 3.14 * self.radius * self.radius  # or self.x*self.x is fine too
    
class Square(Shape):
   def __init__(self,side):
       self.side=side
       super().__init__(side, side)  # x and y both = side
       
       def area(self):
           return self.side * self.side

# Testing
rec = Shape(3, 5)
print("Rectangle area:", rec.area())

circle = Circle(4)
print("Circle area:", circle.area())

sqaure= Square(4)
print("Square area:", sqaure.area())
