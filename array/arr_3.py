# array traversal
import array

arr1= array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('d', [1.5, 2, 3.0, 1.3])

def travers(array):
    for i in array:
        print(i)

travers(arr1)
