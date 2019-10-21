# Setting an initial weight for the pet
# initial_weight = 2

# Function for showing pet weight
# Function to allow user to choose a food and feed pet said food
def user_choice_exercise():
    initial_weight = 2
    # low = 1
    # high = len(FOOD_DICT)
    activity_menu = []
    print("Please choose an option from the following activities:")

    number = 1
    for activity in EXERCISE_DICT:
        print("{}.  {}".format(number, activity.title()))
        number += 1
        activity_menu.append(activity)

    choice = int(input("Please choose an option from the list - type the number >> ", ))
    # "Please choose a number between {} and {}.".format(low, high), low, high)

    chosen_exercise = activity_menu[choice - 1]

    print("Your pet will {}.".format(chosen_exercise.title()))

    initial_weight += EXERCISE_DICT[chosen_exercise] + 0
    # print(initial_weight)

    print("Your pets current weight is {}".format(initial_weight))


EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

user_choice_exercise()
# check_weight()
