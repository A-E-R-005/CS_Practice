# for loop = used to iterate over a sequence (string, list, tuple, set)
#          repeat block of code an exact amount times

name = "Adam Rehman"

for i in range(1,11, 4):
    print(i)

for letter in name:
    print(letter, end="-")

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Happy New Year")