"""
print, type - declare a function, name of function, arguments, scope, return, calling
power of x
concatenating things
length function
default arguments, parameters vs arguments
create an int conversion function
task - login system, traingle
"""


def print_hello():
    print("Hello")


def square(number):
    return number*number


def multiply(x, y):
    return x * y


def concatenate(x, y, z):
    return f"{str(x)} {str(y)} {str(z)}"


def length(arr):
    counter = 0
    for each in arr:
        counter += 1
    return counter


def power_of(num, power=2):
    result = num
    for i in range(1, power):
        result *= num
    return result


def int_conversion(x):
    try:
        return int(x)
    except:
        x = input("Please enter an integer")
        return int_conversion(x)
