# SUPER() Method
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...............")
        return 
    
    @staticmethod
    def stop():
        print("Car Stopped...............")
        return 

class TataMotors(Car):
    def __init__(self, brand, type):
        self.name = brand
        super().__init__(type)
        



Car1 = TataMotors("SAFARI","Petrol")
Car1.start()
print("\nAfter a drive \n")
Car1.stop()
print(Car1.type, Car1.name)