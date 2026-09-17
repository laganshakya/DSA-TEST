# How to use lambda functions in Python

# Lambda functions are anonymous functions that can take any number of arguments but can only have one expression.
# They are often used for short, simple functions that are not reused elsewhere in the code.
# You do not need to give a name to a lambda function, and they are often used as arguments to higher-order functions.

a = lambda x : x + 10
print(a(5))  # Output: 15

print((lambda x, y : x * y)(5, 6))  # Output: 30



x = int(input("Enter a number: "))

y = int(input("Enter another number: "))

print((lambda x, y : x ** y)(x, y))  