first_name = input("Please enter your first name ")
last_name = input("Please enter your last name ")

if first_name == last_name:
    print("first name and last name cannot be same please enter again")
    first_name = input("Please enter your first name ")
    last_name = input("Please enter your last name ")

age = input("Please enter your age ")

if int(age):
    if int(age) >= 18:
        print("welcome")
    else:
        print("You are too young to play this game")
else:
    print('You age must be an integer')
    age = input("Please enter your age ")

# This code has a bug! The problem is if the user does not enter correct detils again
# Then we will run into truble. Another problem is casting age as int, if user enters a string we will get an error. we will look in the next video how to solve this.
