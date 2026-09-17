# To find the key in the given array using binary search
from tracemalloc import start


def binary_search(arr, key):
    index = int
    s = 0
    end = len(arr)-1

    while s <= end :
        mid = (s + end)//2
        #Found
        if arr[mid] == key :
            return mid
        #Still seraching
        elif arr[mid] >= key :
            end = mid -1
            continue
        else :
            s = mid + 1
# Not aviable
    return -1
a = [2,3,4,5,6,7,8,9,10]
b = int(7)
print(binary_search(a,b))