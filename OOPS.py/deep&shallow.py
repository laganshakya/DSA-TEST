a = [1,2,34,5,6,7,8,9,100]
c = []
b = []

# C is the example of deep copy (Change after the creation of c will NOT affect a and vice versa) .

for i in a:
    c.append(i)

# B is the example of shallow copy (Change after the creation of b will affect a and vice versa) .

b = a

a[0] = 10000

print(a)
print(b)
print(c)