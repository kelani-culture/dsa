# returns key with highest value

def max_value_key(mydict):
    a = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
    return a[0][0]
my_dict = {'a': 5, 'b': 9, 'c': 2}

print(max_value_key(my_dict))
