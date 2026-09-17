# Method Overriding in Python

class Animal :
    def eat(self):
        print("Eats")
    def breathe(self):
        print("Breathes")

# It is an example of method overriding in python.


class Deer(Animal):

    def eat(self):
        print("Eats grass")

print("Method Overriding in Python")
a = Deer()
a.eat()