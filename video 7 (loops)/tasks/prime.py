while True:
    try:
        x = abs(int(input("Enter an integer")))
        break
    except:
        print("please enter an int value")

for i in range(2, x//2):
    if x % i == 0:
        print("no")
        break
else:
    print("yes")
