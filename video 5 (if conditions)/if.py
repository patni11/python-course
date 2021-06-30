"""
boolean

if statements - explain indentation, explain colon, explain what's inside if and what's not, not equal

nested if

if else

'and' and 'or' and 'not'

fizz buzz

Create a game login  system
Username - check for age, user have not entered something wrong
Then concatenate everything and give an output
"""

# Boolean
"""
a = 5
b = 5
print(a != b)
"""

# If
"""
num = int(input("please input a number"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
"""

# nested if
"""
x = int(input("Enter a number"))
y = int(input("Enter another number"))

if x % 2 == 0:
    if y % 2 == 0:
        print(x * y)
    else:
        print("y must be even")
else:
    if y % 2 != 0:
        print(x * y)
    else:
        print("y must be odd")
"""

"""
marks = int(input("Enter your marks"))
if marks > 100:
    print("that's not possible")
elif marks < 90 and marks > 80:
    print("good job")
elif marks < 80 and marks > 70:
    print("average")
elif marks > 90:
    print("excelent")
else:
    print("please work harder")
"""
