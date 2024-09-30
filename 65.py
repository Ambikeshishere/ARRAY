'''Define a Circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a perimeter() method of the class which allows you to calculate the perimeter of the circle.'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        print(3.14*self.radius*self.radius)

Circle1 = Circle(5)
print(Circle1.Area())