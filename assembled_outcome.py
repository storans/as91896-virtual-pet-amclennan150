# Making the main menu where the user can choose to see the current pet weight, exercise, see the help info or quit the game


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


def check_float(question, error, low, high):
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


# print welcoming message along with how the game works
def help_info():
    print("\n"
          "Welcome to your own virtual pet!\n"
          "You will be able to choose your pets name along with their beginning weight\n"
          "For your pet to survive it must be kept between a weight of 1.5kg and 2.5kg, don't worry we'll tell you if your pet is near these")


def check_float(question, error, low, high):  # Question and error allow it to be used for various questions
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


def set_weight():
    weight = check_float("Enter the weight of your virtual pet to beginning with (between 1.5 and 2.5) ",
                         "Whoops please enter a number between 1.5 and 2.5", 1.5, 2.5)
    return weight


# Function to allow user to choose a food and feed pet said food

def user_choice_food(weight):
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

    # change_weight(pet_weight, chosen_food)
    weight += FOOD_DICT[chosen_food]

    return weight


# Function to allow user to choose a food and feed pet said food

def user_choice_exercise(weight):
    activity_menu = []
    print("Please choose an option from the following activities:")

    number = 1
    for activity in EXERCISE_DICT:
        print("{}.  {}".format(number, activity.title()))
        number += 1
        activity_menu.append(activity)

    choice = check_int("Please choose an option from the list - type the number >> ",
                       "Please choose a number between 1 and 5.", 1, 5)

    chosen_activity = activity_menu[choice - 1]

    print("Your pet will do {}.".format(chosen_activity.title()))

    weight += EXERCISE_DICT[chosen_activity]

    return weight


def death_checker(weight, pet_alive):
    if 1.4 < weight > 2.6:
        print("You must set a goal before entering your points or showing statistics.\n"
              "Choose Option 2 from the main menu to set your goal.")
    elif weight >= 2.6:
        print("You fed your pet too much and they died")
        pet_alive = False

    else:
        print("You didn't feed your pet enough and they died.")

    return weight


# menu for the user to choose an option
if __name__ == "__main__":

    FOOD_DICT = {"Carrots": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3, "Chocolate": 0.4}
    EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

    pet_weight = 0
    alive = True
    while alive:

        # Start an infinite loop to prompt for a correct option value
        while True:
            # Create an option variable to store the user's chosen option.
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
                print(pet_weight)

            if option == 2:
                print()
                pet_weight = user_choice_food(pet_weight)


            if option == 3:
                print()
                pet_weight = user_choice_exercise(pet_weight)

            if option == 4:
                help_info()

            if option == 5:
                keep_going = False
                break

    print("Thanks for playing")
