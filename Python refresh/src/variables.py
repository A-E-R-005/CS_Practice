# variable - a reusable container for a value (string, integer, float, boolean)
# the variable behaves as if it was the value that it contains

full_name = "Adam Rehman"
age = 21
gpa = 3.2
isStudent = True

print (f"Hello {full_name}")
print(f"You are {age} years old")
print(f"Your gpa is: {gpa}")
print(f"Are you a student?: {isStudent}")

if isStudent:
    print("You are a student")
else:
    print("You are not a student")
