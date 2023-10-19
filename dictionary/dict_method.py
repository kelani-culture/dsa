my_dict = {'name':  'Edy', 'age':26, 'address':'London', 'education': 'master'}
newDict = {}.fromkeys([1, 2, 3], 0)
print(newDict)

# get method
a = my_dict.get('city', 27)
print(a)

# items method
print(my_dict.items())

# keys method
print(my_dict.keys())

# popitem
print(my_dict.popitem())
print(my_dict)

# set default
print(my_dict.setdefault('name1', 'added'))
print(my_dict, '---')

# pop method
my_dict.pop('name1')
print(my_dict)

# update method
my_dict.update({'a':'b','c':'d'})
print(my_dict)
