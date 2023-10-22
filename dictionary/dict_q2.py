# merge two dict and sum up values of common keys

def merge_dicts(dict1, dict2):
    for key, val in dict2.items():
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1.setdefault(key, val)
    return dict1

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))
