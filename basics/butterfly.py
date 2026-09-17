a = int(input("Enter the no.:"))

for i in range(1,a+1):
    b=2*(a-i)
    if b >= 0 :
        print( "*"*i + " "*(b) + "*"*i)
        

    else :
        break

for i in range(a,0,-1):
    b = 2*(a-i)
    if b<= 2*a :
        print( "*"*i + " "*(b) + "*"*i)
        
    else :
        break
