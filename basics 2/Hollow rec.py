# print hollo rectangle 


a = int(input("no. of rows"))

b = int(input("no. of columns"))

for i in range(1,a+1):
    if i == 1 or i == (a) :
        print("*"*(b))
        
    else :
        print("*" + " "*(b-2) + "*")
        # print("*",end="")
        # print(" "*(b-2),end="")
        # print("*")
