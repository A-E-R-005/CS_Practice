import numpy as np
# multidimensional arrays

# 1 dimensional array
array1 = np.array(['A', 'B', 'C'])

# 2 dimensional array
array2 = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])

# 3 dimensional array
array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]])

array3d = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

# etc ......


print(array3d.shape) # (layers, rows, columns)
print(array1.ndim)
print(array3d[0,1,2]) # comma-separated indexing

word = array3d[0,0,0] + array3d[2,0,0] + array3d[2,1,2]

print(word)