

#a = int(input("Enter the no."))
#for j in range(0,a):
#    for i in range(a-j,0,-1):
#        print(i,end="")
#    print()


# If want 1234..123..12...1 then use this


a = int(input("Enter the no."))
for j in range(0,a):
    for i in range(1,a+1-j):
        print(i,end="")
    print()