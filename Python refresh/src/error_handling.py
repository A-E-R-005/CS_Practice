a, b = 10, 15

#try:
#    print(a+b)
#except Exception as e:
#    print(f"Something went wrong: {e}")

try:
    print(a+b)
except TypeError as e:
    print("Please enter a valid integer or float")

print("Continuing with the program")