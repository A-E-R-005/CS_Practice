import numpy as np

# Scalar arithmetic

#array = np.array([1,2,3])

#print(array + 1)
#print(array - 2)
#print(array * 3)
#print(array / 4)
#print(array ** 5)

# all values in the array have these operations performed on them

########################################################

# Vectorized math functions

#array = np.array([1.01,2.5,3.99])

#print(np.sqrt(array))
#print(np.round(array)) # for rounding
#print(np.floor(array)) # alwaays rounds down
#print(np.ceil(array)) # always rounds up
#print(np.pi) # pi

# Excercise
# pi r^2

#radii = np.array([1,2,3])

#print(np.pi * radii ** 2)

#######################################################

# Element-wise arithmetic

#array1 = np.array([1,2,3])
#array2 = np.array([4,5,6])

#print(array1 + array2)
#print(array1 - array2)
#print(array1 * array2)
#print(array1 / array2)
#print(array1 ** array2)

# Each corresponding value will perform the operation with eachother
# so [0,0] from array 1 perfroms the operation with [0,0] of array2 

#######################################################

#Comparison operators

#scores = np.array([91, 55, 100, 73, 82, 64])

#print(scores == 100) # returns boolean array of true or false
#print(scores >= 60)
#print(scores < 60)

#conditional assignment

#scores[scores < 60] = 0 # makes any score less than 60 a 0 showing they failed
#print(scores)