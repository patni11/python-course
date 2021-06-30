from typing import final

first_name = input("Please enter your first name ")
last_name = input("Please enter your last name ")

if first_name == last_name:
    print("first name and last name cannot be same please enter again")
    first_name = input("Please enter your first name ")
    last_name = input("Please enter your last name ")

age = input("Please enter your age ")

try:
    age = int(age)
except:
    print('You age must be an integer')
    age = input("Please enter your age ")
else:
    if age >= 18:
        print("welcome")
    else:
        print("You are too young to play this game")
finally:
    print("the program has ended")

# This code has a bug! The problem is if the user does not enter correct detils again
# Then we will run into truble. The casting into int problem is temporarily solved but if user enters something wrong again, we will get an error
