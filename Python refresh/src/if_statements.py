# if statements = execute some code only if a condition is True
#                they allow for basic decision making
#                (if, elid, else)

age = int(input("Enter your age: "))
has_ticket = True
price = 10.00

if age >= 65:
    print("You are a senior citizen")
    print(f"Your ticket price for a senior citizen is: ${price * 0.75}")
elif age >= 18:
    print("You are an adult")
    print(f"Your ticket price for an adult is: ${price}")
elif age < 0:
    print("you havent been born yet")
elif age == 0:
    print("you were just born")
else:
    print("You are a child")
    print(f"your ticket price for a child is: ${price * 0.5}")


if has_ticket:
    print("You can enter the concert")
else:
    print("you need to buy a ticket")