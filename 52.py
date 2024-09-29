# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then Create a method to print the average.

class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,",self.name, "your avg score is :", sum/3)
s1 = Student("Ambikesh", [99,98,97])
s1.get_avg()
