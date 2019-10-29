# Setting an initial weight for the pet

# Function to check user input is a whole number
def check_int(question, error, low, high):  # Question and error allow it to be used in a range of situations

    valid = False

    while not valid:
        number = input("{} >> ".format(question))  # Any question that needs a whole number for the input
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)


# Function for showing pet weight
# Function to allow user to choose a food and feed pet said food
def user_choice_exercise():
    initial_weight = 2
    low = 1
    high = 4
    activity_menu = []
    print("Please choose an option from the following activities:")

    number = 1
    for activity in EXERCISE_DICT:
        print("{}.  {}".format(number, activity.title()))
        number += 1
        activity_menu.append(activity)

    choice = check_int("Please choose an option from the list - type the number >> ",
                       "Please choose a number between 1 and 4.", low, high)

    chosen_exercise = activity_menu[choice - 1]

    print("Your pet will {}.".format(chosen_exercise.title()))

    initial_weight += EXERCISE_DICT[chosen_exercise]


    #print("Your pets current weight is {}".format(initial_weight))


EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

user_choice_exercise()
