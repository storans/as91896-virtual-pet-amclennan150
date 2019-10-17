
def check_float(question, error, low, high):  # Question and error allow it to be used in a range of situations
    valid = False

    while not valid:
        number = input("{} >> ".format(question))  # Any question that needs a number as the input
        try:
            number = float(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)


def check_int(question, error, low, high):  # Question and error allow it to be used in a range of situations
    valid = False

    while not valid:
        number = input("{} >> ".format(question))  # Any question that needs a number for the input
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)


# Function to allow user to choose a food and feed pet said food
def user_choice_food():
    low = 1
    high = len(FOOD_DICT)
    food_menu = []
    print("Please choose an option from the following foods:")

    number = 1
    for food in FOOD_DICT:
        print("{}.  {}".format(number, food.title()))
        number += 1
        food_menu.append(food)

    choice = check_int("Please choose an option from the list - type the number",
                       "Please choose a number between {} and {}.".format(low, high), low, high)

    chosen_food = food_menu[choice - 1]

    print("You will feed your pet {}.".format(chosen_food.title()))


# Function to allow user to choose an activity and exercise pet

def user_choice_exercise():
    low = 1
    high = len(EXERCISE_DICT)
    exercise_menu = []
    print("Please choose an option from the following foods:")

    number = 1
    for activity in EXERCISE_DICT:
        print("{}.  {}".format(number, activity.title()))
        number += 1
        exercise_menu.append(activity)

    choice = check_int("Please choose an option from the list - type the number",
                       "Please choose a number between {} and {}.".format(low, high), low, high)

    chosen_exercise = exercise_menu[choice - 1]

    print("Your pet will {}.".format(chosen_exercise.title()))


# Getting the user to name their pet
name = input("What would you like to name your pet? >> ")

# Getting the user to input their virtual pets starting weight by running through the function
initial_weight = check_float("Enter the weight of your virtual pet to beginning with (between 1.5 and 2.5) ",
                             "Whoops please enter a number between 1.5 and 2.5", 1.5, 2.5)

print(initial_weight)

# Printing the users input
print("The beginning weight of {} is {}.".format(name, initial_weight))

EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}
FOOD_DICT = {"Carrots": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3, "Chocolate": 0.4}



user_choice_exercise()

user_choice_food()
