# searching in an array using simple/linear search
import array
ma = array.array('i', [1, 2, 3, 4, 5])

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
           return 'located at index ' + str(i)
    return -1

print(linear_search(ma, 5))
