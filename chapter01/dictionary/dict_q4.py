# reverse key value pairs

def reverse_dict(my_dict):
    a = {val:key for key, val in my_dict.items()}
    return a

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
