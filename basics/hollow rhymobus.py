#Hollow rhymobnus

a = int(input("enter the no.:"))
for i in range(0,a+1):
    if i == 0 or i == a :
        print( " "*(a-i) +  "*"*a)
    else :
        print( " "*(a-i) + "*" + " "*(a-2) + "*")