def middle(lst):
    lst.remove(lst[0])
    lst.remove(lst[len(lst)-1])
    return lst

a = [1, 2, 3, 4]
print(middle(a))