# Making the main menu where the user can choose to see the current pet weight, exercise, see the help info or quit the game
initial_weight = 2

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


# Function to allow user to choose a food and feed pet said food

def user_choice_food():

    new_weight = initial_weight
    food_menu = []
    print("Please choose an option from the following foods:")

    number = 1
    for food in FOOD_DICT:
        print("{}.  {}".format(number, food.title()))
        number += 1
        food_menu.append(food)



    choice = check_int("Please choose an option from the list - type the number >>",
                       "Please choose a number between 1 and 5.", 1, 5)

    chosen_food = food_menu[choice - 1]

    print("You will feed your pet {}.".format(chosen_food.title()))

    new_weight += FOOD_DICT[chosen_food]


    # Function to allow user to choose a food and feed pet said food


def user_choice_exercise():
    activity_menu = []
    print("Please choose an option from the following activities:")

    number = 1
    for activity in EXERCISE_DICT:
        print("{}.  {}".format(number, activity.title()))
        number += 1
        activity_menu.append(activity)


    choice = check_int("Please choose an option from the list - type the number >> ","Please choose a number between 1 and 5.", 1, 5 )


# menu for the user to choose an option

FOOD_DICT = {"Carrots": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3, "Chocolate": 0.4}

EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

user_goal = None
total_exercise = None

print()
print("-" * 20)
print()
print("Please choose an option from the following menu:")
print("1. Show current weight\n"
      "2. Feed Pet\n"
      "3. Exercise Pet\n"
      "4. See help information\n"
      "5. Exit\n")
option = check_int("Enter your choice: ", "You must choose a number between 1 and 5.", 1, 5)

if option == 1:
    print("Show current weight")

if option == 2:
    print("Feed Pet")

if option == 3:
    print("Exercise Pet")

if option == 4:
    print("Help Information")

if option == 5:
    print("End Game")
