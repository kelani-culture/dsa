import array

my_array = array.array('i')
print(my_array)
my_array1 = array.array('i', [1, 2, 3, 4, 5])
print(my_array1)
# another module for creating array

import numpy as np
np_arr = np.array([], dtype=int)
np_arr1 = np.array([1, 2, 3], dtype=int)
print(np_arr1)
