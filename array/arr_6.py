import array
# Add items from list into array using fromlist() method
my_array = array.array('i')
templist = [20, 21, 22]
my_array.fromlist(templist)
print(my_array)

# remove any array element using remove()
my_array.remove(22)
print(my_array)

# extend array
my_array.extend([1, 2, 3, 4, 5, 6, 7])
print(my_array)

# remove last element using pop
my_array.pop()
print(my_array)

# fetch any element using index method
print(my_array.index(21))

# reverse a python array using reverse()
my_array.reverse()
print(my_array)

# get array buffer information through buffer_info()
print(my_array.buffer_info())

# check for numbebr of occurences of an element using count()
my_array.append(2)
print(my_array.count(2))

#convert array to string using
strTemp = bytearray(my_array)
arry = array.array('i')
arry.frombytes(strTemp)
print(arry)
 #  convert array to list
print(my_array.tolist())

# slice element on an array
print(my_array[1:4])
