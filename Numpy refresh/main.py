import numpy as np

#print(np.__version__)

#my_list = [1, 2, 3, 4] *2  #duplicates elements
#array = np.array([1, 2, 3, 4]) * 2 #multiplies each element
#print(my_list)
#print(array)
#print(type(array))


###########################################
# slicing using numpy

array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])

# array[start:end:step]
# positive to go through the array forwards
# negative to go backwards back through the array for 3 down
print(array[1:]) # selects everything up until the end
# array[start:end:step]
print(array[0:4:2]) # selects everything from arrays 0 til 4, giving every second row
print(array[::-2]) # selects everything from arrays 0 to 4, but having a negative means output is reversed
