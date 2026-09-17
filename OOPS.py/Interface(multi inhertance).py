# Example of multiple inheritance in Python .
# Since Python doesn't support interface and implementation, we can use multiple inheritance to achieve the same functionality.

class Herbivore:
    def eat(self):
        print("This animal eats plant.")
        pass


class Carnivore:
    def eat(self):
        print("This animal eats meat.")
        pass

class Bear(Herbivore, Carnivore):
    def eat(self):
        Herbivore.eat(self)
        Carnivore.eat(self)

Bear().eat() 

# Output: Bear eats both plants and meat.