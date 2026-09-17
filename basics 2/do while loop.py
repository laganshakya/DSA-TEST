while (True) :

    a = int(input("enter the number which is not divisible by 10 :"))

    if a % 10 == 0 :
        break
    
    print(a)

# Do-while loop in python is not directly available, but we can simulate it using a while loop.
# The above code is an example of a do-while loop in Python. It will keep asking the user to enter a number until the user enters a number 
# That is divisible by 10. When the user enters a number that is divisible by 10, the loop will break and the program will end.

# do :
#     if a % 10 == 0 :
#         break
#     else :
#         print(a)
# while (condition) :