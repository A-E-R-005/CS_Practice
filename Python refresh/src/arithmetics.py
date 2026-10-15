# arithmetic = + addition
#              - subtraction
#              * multiplication
#              / division (returns a float)
#              // integer division (returns an integer)
#              % modulus (returns the remainder)

friends = 5

friends = friends + 1
friends +=1                     # augmented assignment operator

friends = friends - 1
friends -=1

friends = friends * 2
friends *=2

friends = friends / 2
friends /=2

friends = friends // 2
friends //=2

remaining_friends = friends % 3

print(friends)
print(remaining_friends)