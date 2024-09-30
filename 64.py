# Creating vector units

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def showVectors(self):
        print(self.x, "i +", self.y, "j +", self.z,"k" )

num1 = Vector(4,5,9)
num1.showVectors()
