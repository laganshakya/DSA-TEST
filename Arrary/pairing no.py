#Pairing of no. in the given array
a = []
while True:
    b = int(input("Enter the number of elements in the array: "))
    a.append(b)
    c = input("continue (y/n) :")
    if c == 'n':
        break
print(a)
for i in range(0, len(a) + 1) :
    for j in range(i+1, len(a)):
        if j <= len(a) and i < (len(a)-1) and j < len(a):
            print("(", a[i], ",", a[j], ")")
        else :
            break