# Class Method

class Person:
    name = "Ambikesh"

    #def changeName(self, name):
        #Person.name = name
        #self.name = name
        #self.__class__.name = name
    
# Class Method

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Toni Stark")
print(p1.name)
