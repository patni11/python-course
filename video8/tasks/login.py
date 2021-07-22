def get_age():
    try:
        age = int(input("Enter your age  "))
        return age
    except:
        print("age must be a whole number, please try again  ")
        return get_age()


def concatenate(first_name, last_name, age):
    return f"welcome {first_name} {last_name}! You are {str(age)}"


def allowed_to_play(age, required_age=18):
    if (age < required_age):
        return False
    else:
        return True


def login():
    first_name = input("Enter your first name  ")
    last_name = input("Enter your last name  ")
    age = get_age()

    if allowed_to_play(age):
        print(concatenate(first_name, last_name, age))
    else:
        print("sry you must be above 18")


login()
