"""
While loops homework example - when teacher asks you to write 100 lines of 'I will not forget to finish my homework' - 

for loops printing even numbers with range

For loops with arrays and dictionaries - printing multiple values, getting the len of arrays.

nested loops

break and else

Task - prime or not

Fibonacci series
"""

# While loops
"""
x = 100
i = 1
while i <= x:
    # str(i) + "I will finish my homework"
    print(f"{i} I will finish my homework")
    i += 1  # i = i + 1
"""

# For Loops
"""
n = int(input("Enter a number"))
for i in range(0, n+1, 2):
    print(i)
"""
'''
arr = []
for i in range(1, 10+1):
    arr.append(i)

dicionary = {}
for i in range(0, 100, 2):
    dicionary[i] = i+4

for each in dicionary.values():
    print(each)

i = 0
for each in arr:
    i += 1
print(i)
'''

# nested loop
'''
x = [2, 4, 6, 8]
y = [3, 5, 7, 9]

for i in x:
    for j in y:
            print(i * j)
'''

# break and else
'''
x = [1, 2, 3, 4, 5, 6]
for each in x:
    print(each)
else:
    print("we do not have break")
'''
