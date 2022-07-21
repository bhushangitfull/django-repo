class Sample():
    pass

x = Sample()

print(type(x))


class Dog():
    type = "carnivorus"
    def __init__(self, breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "lab", name="bruno")
myfav_dog = Dog(breed = "german sheepherd", name="shagy")
print(myfav_dog.breed)
print(mydog.name)
print(mydog.breed)
print(mydog.type)


#Circle class

class Circle():
    pi = 3.14
    def __init__(self, radius = 1):
     
        self.radius = radius

    def area(self):
        return  self.radius*self.radius*Circle.pi
    
    def set_radius(self,new_r):
        self.radius = new_r

mycircle = Circle()
mycircle.set_radius(56)
print(mycircle.radius) 
print(mycircle.area())      



