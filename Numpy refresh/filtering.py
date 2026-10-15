import numpy as np

# Filtering = refers to the process of selecting elements
#           from an array that match a given condition

#ages = np.array([[21,17,19,20,16,30,18,65],
#                 [39,22,15,99,18,19,20,21]])

#teenagers = ages[ages < 18] # new array that meets the condition
#adults = ages[(ages >= 18) & (ages < 65)] # uses C & to combine because numpy built in c instead of python which is and
#adults = ages[(ages < 18) | (ages >=65)] # can use an or statement but conditions then change
#seniors = ages[ages >= 65]
#evens = ages[ages%2 == 0]
#odds = ages[ages%2 != 0]


#print(teenagers) # boolean indexing - flattening the array to 1 dimension
#print(adults)
#print(seniors)
#print(evens)
#print(odds)

#adults = np.where(ages >= 18, ages, 0) # keeps original shape of data - but slower than boolean indexing
#print(adults)