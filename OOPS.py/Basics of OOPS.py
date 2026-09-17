# This is example of classes in java

# class OOPS {

# }

# class Pen {
#     

#     string colour;
#     string tip;

#     void setcolour(string newcolour) {
#         colour = newcolour;
#     }

#     void newtip(string newtip) {
#         tip = newtip;
#     }
# }

# This is example of classes in python

class Pen :

    # Properties + Functions

    colour = "Blue"
    tip = 5


    def info(self, colour, tip):
        print("Colour of pen is",colour)
        print("Tip of pen is",tip)


a = Pen()
b = Pen()

print(a.colour,a.tip)



a.info("yellow", 2)
b.info("red", 3)

# Calling the properties of the class Pen

a.colour = "Green"
a.tip = 3

# Changing the values of the properties

print(a.colour,a.tip)

# Public , protected and private Access Modifiers
# Since python is great language ,  it does not have protected .
# We do not have to use anything for public access modifier. It is by default public in python
# For private access modifier we use __ (double underscore) before the property name. It is called name mangling in python.
# It is not a strict private access modifier like java or c++ but it is a way to avoid accidental access of the property from outside the class.

print("\n\n\n")

# This "__init__" is a constructor in python. It is called when we create an object of the class. It is used to initialize the properties of the class.

class BankAccount:

    def __init__(self, account_number, balance):

        self.account_number = account_number
        self.__balance = balance

BankAccount1 = BankAccount("1234567890", 1000) 

print("Account Number:" , BankAccount1.account_number)

# Outside the class we cannot access the private property __balance directly. It will give an error if we try to access it directly.

print("Balance:" ,BankAccount1.__balance) # This will give an error

# But we can access the private property __balance using name mangling. The name of the private property is changed to _ClassName__PropertyName.
# So we can access it like this:-

print("Balance:" ,BankAccount1._BankAccount__balance)