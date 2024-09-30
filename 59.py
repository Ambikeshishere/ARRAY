#multilevel inheritence
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
    def __init__(self, brand):
        self.name = brand
        
class Safari(TataMotors):
    def __init__(self, type):
        self.type = type


Car1 = Safari("Diesel")
Car1.start()
print("\nAfter a drive \n")
Car1.stop()