class Animal:
    def eat(self):
        print("Animal is eating")

    def abstract_walk(self):
        # raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def walk(self):
        print("Dog is walking")

a = Animal()

b = Dog()

print(a.eat())
print(b.walk())