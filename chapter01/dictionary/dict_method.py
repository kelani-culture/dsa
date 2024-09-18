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

# all function
my_dict1 = {

        -1: "three",
        5: "five",
        2: 'two',
        3: 'three',
        6: 'six',
        }
# if dict contains 0 return false
# if dict contain False return False
# if dict is not 0 return true
# if dict is not false return true
print(all(my_dict1))

# any function

my_dict1 = {

        0: "three",
        0: "five",
        0: 'two',
        0: 'three',
        True: 'six',
        }
# if dict contains number > 0 or 0 will return true
# if dict contains only key 0 will return false
# if dict does not contain true will return false
# if dict contains contain true will return true
print(any(my_dict1), 'any')
