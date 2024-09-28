# init function

class student:
    
    def __init__(self, fullname):
        self.name = fullname
        print("Loading DATABASE.................")
new = input("Enter the name of student\n")
s1 = student(new)
print(s1.name)
