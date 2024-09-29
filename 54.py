class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.brk = True
        self.clutch = True
        print("Car Started...............")

        car1 = Car()
        car1.start()