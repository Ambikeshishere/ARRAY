# init function

class student:
    
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Loading DATABASE.................")
new = input("Enter the name of student\n")
mark = input("Enter the name of student\n")
s1 = student(new, mark)
print(s1.name)
print(s1.marks)

print(s1.name,s1.marks)
