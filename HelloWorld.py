""" Python Method overriding = is the ability of an OOP language to allow a subclass aka a Child Class
 to provide a specific implementation of a method that is already provided by one of its parents. In this case 
 we are going to override the eat method.
 Basically speaking an object will use a method that is more closely associated with itself first before relying
 on a method that it may inherit from a parent class"""
class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot.")
rabbit = Rabbit()
rabbit.eat()

# Method chaining = calling multiple methods sequentially ,
#  each call performs an action on the same object and returns self.
class Car:
    def turn_on(self):
        print("You turn on the engine.")
        return self
    def drive(self):
        print("You drive the car.")
        return self
    def brake(self):
        print("You step on the braakes.")
        return self
    def turn_off(self):
        print("You turn off the engine.")
        return self
car = Car()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

# Super () = super functions are used to give access to the methods of a parent class.
# returns a temporary object of a parent class when used.
class Rectangle():
        
        def __init__(self,length,width):
            self.length = length
            self.width = width
class Square(Rectangle):

    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
         return self.length*self.width
    
class Cube(Rectangle):

    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
         return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(4,4,4)
print(square.area())
print(cube.volume())

# THis is an example of speech syunthesis in English.






