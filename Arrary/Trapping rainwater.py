#Trapping rainwater problem

# GREAT CONCEPT AND CODE

# Width = 1 unit
#Lmax helper arrary

a = [4,2,0,6,3,2,5]
n = len(a)
lmax = [0]*n
lmax[0] = (a[0])
for i in range(1,n):
    lmax[i] = (max(a[i], lmax[i-1]))

print(lmax)

#Rmax helper arrary

rmax = [0]*n
rmax[n-1] = (a[n-1])
for i in range(n-2,0,-1):
    rmax[i] = (max(a[i],rmax[i+1]))
print(rmax)

#Water stored 

tw = 0
for i in range(0,n-1):
    c = min(lmax[i],rmax[i])
    if c - a[i] >= 0 :
        tw = tw + (c-a[i])
print("final value:",tw)