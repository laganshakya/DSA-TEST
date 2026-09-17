a = int(input("enter the number of rows :"))
ch=0
for i in range(1,a+1) :

    for j in range(1,i+1) :
            
            print(chr(ord('A') + ch), end = " ")
            ch += 1
            ch%=26

    print()