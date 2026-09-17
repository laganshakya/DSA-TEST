# Parent class

class Animal :
    def eat(self):
        print("Eats")
    def breathe(self):
        print("Breathes")

# Subclass (inherited from Animal)
# In java we use extends keyword to inherit a class but in python we use parenthesis to inherit a class.


class Fish(Animal):

    def fins(self) :
        print("for swimming")

class Mammal(Animal):

    def legs(self,a) :
        print("for walking use" + str(a) + " legs")

class dogs(Mammal):

    def bark(self):
        print("barks")

    def color(self,color):
        print(color)
    



puffer = Fish()
a = Fish()
b = Mammal()
c = dogs()

a.eat()

a.breathe()

b.eat()
b.legs(4)

puffer.fins()

# Taking the object of child class and calling the methods of parent class and child class.

c.bark()
c.color("white")
c.eat()