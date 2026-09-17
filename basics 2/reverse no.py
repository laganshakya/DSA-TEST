# Reverse the given number.

a = int(input("enter the number which want to reverse :"))

c = ""

while a > 0 :

    b = a % 10

    a = a // 10

    c = str(c) + str(b)

print(c)