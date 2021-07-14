"""
print, type - declare a function, name of function, arguments, scope, return, calling
power of x
concatenating things
length function
default arguments, parameters vs arguments
create an int conversion function
task - login system, traingle
"""

"""
def print_hello():
    print("Hello")


print(print_hello())
"""

"""
def square(number):
    return number*number


result = square(5)
print(result)
"""
"""
x = int(input("Enter a number "))
y = int(input("Enter a number "))
z = 10

def multiply(x, y):
    print(z)
    return x * y

print(x)
print(multiply(x, y))
"""

"""
def concatenate(x, y, z):
    return f"{str(x)} {str(y)} {str(z)}"


print(concatenate("shubh", "patni", "course"))
"""

"""
def length(arr):
    counter = 0
    for each in arr:
        counter += 1
    return counter


arr = [1, 2, 3, 4, 5, 6, 7]
print(length(arr))
"""

"""
def power_of(num, power=2):
    result = num
    for i in range(1, power):
        result *= num
    return result


num = int(input("Enter a number  "))
power = int(input("Enter a power  "))
print(power_of(num, power))
"""

"""
def int_conversion(x):
    try:
        return int(x)
    except:
        x = input("Please enter an integer")
        return int_conversion(x)


x = int_conversion(input("Please etner a number"))
print(x)
"""
