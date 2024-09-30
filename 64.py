# Creating vector units

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def showVectors(self):
        print(self.x, "i +", self.y, "j +", self.z,"k" )

    def __add__(self , num2):
        newx = self.x + num2.x
        newy = self.y + num2.y
        newz = self.z + num2.z

        return Vector(newx,newy,newz)
    
    def __sub__(self , num2):
        newx = self.x - num2.x
        newy = self.y - num2.y
        newz = self.z - num2.z

        return Vector(newx,newy,newz)


num1 = Vector(4,5,9)
num1.showVectors()


num2 = Vector(8,15,91)
num2.showVectors()

num3 = num1 + num2
num3.showVectors()

num4 = num1 - num2
num4.showVectors()