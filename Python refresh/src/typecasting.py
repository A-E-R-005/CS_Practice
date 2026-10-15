# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Adam Rehman"
age = 21
gpa = 4.0
is_student = True

print(type(name))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
age += "1"
print(age)
print(type(age))


name = bool(name) # Always true unless the variable is empty therefore can check if someone has inputted their username or similar cases
print(name)
