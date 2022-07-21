class Animal():
    def __init__(self):
        print("animal created")

    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("eanting")




class Cow(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("cow created")
    
    def grasppin(self):
        print("cow in graspping")


mymow = Cow()
mymow.whoAmI()
mymow.eat()
mymow.grasppin()