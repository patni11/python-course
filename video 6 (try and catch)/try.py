"""
try except
else
finally

Variable not defined
Cannot add string and int
Arr does not exists 
Else if no errors are raised
trying to use string as int
"""

# try except
"""
try:
    print(x)
except:
    print("X does not exist")

y = 18
print(y)
"""

# else
"""
try:
    x = int(input("Enter a number"))
    y = int(input("Enter a number"))
except:
    print("either y or x is not an integer")
else:
    print(x+y)
"""

# Finally
"""
arr = [1, 2, 3, 4, 5, 6]

try:
    arr[5] = arr[7]
except:
    print("The index probably does not exist")
    try:
        arr[6] = int(input("enter a number"))
    except:
        print("you must enter an integer")
else:
    try:
        a = "shubh"
        arr[6] = a
    except:
        print("There was an error")
finally:
    print("Okay this was too much, you enter your own array")
    arr = input("Please enter values followed by space").split()

print(arr)
"""
