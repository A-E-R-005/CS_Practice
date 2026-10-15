import numpy as np

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# The dimensions have the same size
# OR
# One of the dimensions has a size of 1

#array1 = np.array([[1,2,3,4]])
#array1 = np.array([[1,2,3,4],
#                   [5,6,7,8]]) # this will fail broadcasting because the shape is now (2,4) 
                               # because the rows are neither the same nor is one of the a 1
#array1 = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])
#array2 = np.array([[1], [2], [3], [4]])
#array2 = np.array([[1,2], [2,3], [3,4], [4,5]]) # this will now fail as the shape does not match it is now
                                                # [4,4] and [4,2] it is not a 1 nor equal to 4 for columns

#print(array1.shape)
#print(array2.shape)


#print(array1 * array2)

#array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
#array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

#print(array1 *array2)