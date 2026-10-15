# List []  = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable (add / remove), unordered, so indexing does not work or item assignment
#               No duplicated, best for membership training

fruits = ["apple", "orange", "bannana", "coconut"] # list

print(fruits[1])

fruits[0] = "pear"
fruits.append("mango")
fruits.remove("orange") #removes via value
fruits.pop(2) # removes via index
fruits.clear()

for fruit in fruits:
    print(fruit, end=" ")


fruits.clear()

fruits = ("apple", "orange", "bannana", "coconut") # tuple
print(fruits[1])
for fruit in fruits:
    print(fruit, end=" ")


fruits.clear()

fruits = {"apple", "orange", "bannana", "coconut"} # set

fruits.add("mango")
fruits.remove("orange")
fruits.clear()

for fruit in fruits:
    print(fruit, end=" ")

fruit = input("Enter a fruit: ")

if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")


