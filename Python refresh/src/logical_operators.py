# logical operators = evauluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the cxondition (not False, not True)

temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print(" The outodoor event is cancelled")
else:
    print("The outdoor event is on")

temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("and it is sunny")
elif temp <=0 and is_sunny:
    print("it is cold outside")
    print("and it is sunny")
#elif temp < 28 and temp > 0 and is_sunny:
elif 28 > temp > 0 and is_sunny:
    print("it is warm outside")
    print("and its sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("and it is  not sunny")
elif temp <=0 and not is_sunny:
    print("it is cold outside")
    print("and it is  not sunny")
#elif temp < 28 and temp > 0 and is_sunny:
elif 28 > temp > 0 and not is_sunny:
    print("it is warm outside")
    print("and its not sunny")