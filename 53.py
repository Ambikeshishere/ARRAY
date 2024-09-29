#Static Method

class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,",self.name, "your avg score is :", sum/3)
s1 = Student("Ambikesh", [99,98,97])

s1.hello()
s1.get_avg()