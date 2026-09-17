n = int(input("Enter the no. of rows:"))
m = int(input("Enter the no. of cols:"))

# Taking input of elements for mat.

b = 0
c = []
while b < n*m :
    a = int(input("Enter nXm numbers:"))
    b += 1
    c.append(a)

# Filling elements in mat.

b = 0
for i in range(0 , n):
    if i != 0 :
        print(" ")
    for j in range(0,m):
        if b <= n*m:
            print(c[b] , end=" ")
            b += 1
        else :
            break