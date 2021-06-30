while True:
    try:
        n = abs(int(input("Enter an integer")))
        break
    except:
        print("please enter an int value")

series = [0, 1]

for i in range(3, n+1):
    series.append(series[i-2]+series[i-3])

print(series)
