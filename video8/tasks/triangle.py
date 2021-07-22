"""
1
12
123
1234
12345
"""


def triangle(steps=5):
    for i in range(1, steps+1):
        print()
        for j in range(0, i):
            print(j+1, end=" ")


steps = int(input("Please enter the number of steps for triangle"))
triangle(steps=steps)
