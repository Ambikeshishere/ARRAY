#inheritence
class Car:
    @staticmethod
    def start():
        print("Car Started...............")
        return 
    
    @staticmethod
    def stop():
        print("Car Stopped...............")
        return 

class TataMotors(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    

Car1 = TataMotors("Safari", "Orange")
Car2 = TataMotors("Harrier", "White")

print(Car1.color, Car1.name, Car1.start() )