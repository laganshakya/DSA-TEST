#array name = array * (array size)

array_list =  [0] * 5
print(array_list)

array_list[0] = "a"
array_list[1] = "b"
array_list[2] = "c"
array_list[3] = "d"
array_list[4] = "e"

print(array_list)

array_list[0] = 1
array_list[1] = 2
array_list[2] = 3
array_list[3] = 4
array_list[4] = 5

print(array_list)

array_list[0] = int(input("Enter the no.:"))
array_list[1] = int(input("Enter the no.:"))
array_list[2] = int(input("Enter the no.:"))
array_list[3] = int(input("Enter the no.:"))
array_list[4] = int(input("Enter the no.:"))

print(array_list)

print(array_list[0])
print(array_list[1])
print(array_list[2])

array_list[2] = array_list[2] + 1

print(array_list)

print("Length of array: " + str(len(array_list)))