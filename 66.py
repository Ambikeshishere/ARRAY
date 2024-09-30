'''Define A Employee class with attributes role, department and salary.
This class also a showDetails() method.
Create an Engineer class that inherits properties from Employee and his additional attributes : name and age.'''

class Employee:
    def __init__(self ,role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def Basics(self, name, age):
        self.name = name
        self.age = age

    def showDetails(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Role = ", self.role)
        print("Department = ", self.dept)
        print("Salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")


e1 = Engineer("Ambikesh" , "40")
e1.showDetails()