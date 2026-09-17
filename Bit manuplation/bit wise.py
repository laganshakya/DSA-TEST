# In this we first convert decimal to binary then add binary then convert back to decimal
# 5 = 101 , 6 = 110 .......... 101 + 110 = 100...... 100 = 4 
# AND 

print(5 & 6)

# In this we first convert decimal to binary then add binary then convert back to decimal
# OR (to type this symbol "|" ----> shift + "\" )

print(5 | 6)

# MSB(len of number place or left most) and LSB(units place or right most) (most and least significant bits) ............
# First take "~" then , Take compliment of number in binary form then and + 1 in binary form then u will get no. and change sign acc. to like if msb is 1 so sign will after compliment 0 then +ve and if msb is 0 as in most case then sifn will be -ve 
# NOT(~)

print(~-2)
print(~2)
print(~0)

# If the both are same then output will be 0 like 1,1 or 0,0 the  ans = 0 if both are differ ans = 1
# XOR(^)

print(5^6)
print(2^7)

# Eg : 5 << 2 then last 2 msb of 5 will remove out and every element shift by 2 places and lsb will return 0 in that empty space
# Sort trick :- to find value direct use this a << b = (a*(2**b))
# LEFT SHIFT(<<)

print(4<<6)
print(7<<5)
print(5<<2)
print(2<<2)


