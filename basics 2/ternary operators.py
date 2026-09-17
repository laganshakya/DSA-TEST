
# Difference between two numbers always positive using ternary operator

a = int(input("Enter a number: "))

b = int(input("Enter another number: "))

c = a - b if a > b else b - a

print("The difference between the two numbers is:", c)