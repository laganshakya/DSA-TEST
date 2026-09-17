def factorial(a) :
    b=1
    for i in range(1,a+1) :
        b = b*i
    return b


# c = int(input("enter the no. :"))
#d = factorial(c)
#print(d)
# Binomial factor  nCr



n = int(input("Enter the value of n:"))
r = int(input("Enter the value of r:"))
if n>=r and n > 0 :
    N = factorial(n)
    R = factorial(r)
    NCR = factorial(n-r)
else :
    print("n can't be smaller than r")

print("nCr value :",N/(NCR*R))