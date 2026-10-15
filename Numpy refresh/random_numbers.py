import numpy as np

# Random Default RNG

#rng = np.random.default_rng(seed=1) # you can set a seed to reproduce the same results otherwise a seed is given by numpy

#print(rng.integers(low=1, high=101)) # allows you to get a random number betwrrn 1 and 100
#print(rng.integers(low=1, high=101, size=3)) # gives you 3 random numbers in 1D array
#print(rng.integers(low=1, high=101, size=(3,2))) # gives the output in a 2D array good for matrices


##################################################################

# Random Uniform 

#np.random.seed(seed=1) # to create the seed for random 

#print(np.random.uniform()) # uniform distribution - gives random floating point nmber
#print(np.random.uniform(low=-1, high=1)) # between -1 and 1
#print(np.random.uniform(low=-1, high=1, size=(3, 2))) # shape(3,2) of floating point numbers between -1 and 1

##################################################################

# Shuffling

rng = np.random.default_rng()

array = np.array([1,2,3,4,5])
rng.shuffle(array) # shuffling the vbalues in the array

print(array)


fruits = np.array(['apple', 'orange', 'bannana', 'coconut', 'pineapple'])
fruit = rng.choice(fruits) # chooses a choice of the array fruits
fruts = rng.choice(fruits, size=3) # chooses three of them
frutis = rng.choice(fruits, size=(3,2)) # chooses many and ordes in rows and columns of shape (3,2)
print(frutis)

