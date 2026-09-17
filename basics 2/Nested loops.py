a = int(input("enter the number of rows :"))

for i in range(1,a+1) :

    for j in range(1,a+2-i) :
        print("*", end = " ")

    print()