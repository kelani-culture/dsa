def first_second(my_list):
    sort = sorted(my_list, reverse=True)[:2]
    max1, max2 = list(set(sort)) 
    return max1, max2
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

print(first_second(myList))