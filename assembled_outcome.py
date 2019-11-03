# assembled outcome with all components together
# importing time to use later
import time


# function for formatting titles
def formatting(character, output):
    print(character * (len(output) + 4))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 4))


# function for welcoming the user to the game
def welcome_info():
    # print welcoming message along with how the game works
    print("Welcome to your own virtual pet!\n"
          ""
          "You will be able to choose your pet rabbit's name along with their "
          "beginning weight.\n"
          "For your pet to survive it must be kept between a weight of "
          "1.5kg and 2.5kg.")

    # giving the user time to read welcome info before the gaming proceeding
    time.sleep(3)


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


# check user input is a float
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


# printing help info for the user
# can be accessed during game if user decides to see it then
def help_info():
    print("For your pet to survive it must be kept between a weight"
          " of 1.5kg and 2.5kg,"
          " don't worry we'll tell you if your pet is near these")


# Getting the user to enter their own name for their pet
def user_enter_name():
    name_pet = input("What would you like to name your pet? >> ")

    # printing the chosen name
    print("Your pets name is {}".format(name_pet))

    # return pets name so can be accessed later
    return name_pet


# function for the user to chooses to name their pet one of the already
# decided names
def chose_name():
    name_option = []
    print("Choose one of the following names:")
    number = 1
    # list foods in a for loop
    for names in NAME_LIST:
        # print the names in the list
        print("{}.  {}".format(number, names.title()))
        number += 1
        name_option.append(names)

    # getting the user to enter the number that corresponds to the name they want to pick
    chosen_name = check_int("Please choose an option from the list - type the "
                            "number >>", "Please choose a number between 1 and 5.",
                            1, 5)

    # so the name of the pet will print on the next line
    name_pet = name_option[chosen_name - 1]

    # printing the chosen name
    print("Your pets name is {}".format(name_pet))

    # return pets name so can be accessed later
    return name_pet


# giving the user the option to either enter their own name for their pet
# or choose from a given list
def user_choice_name():
    print("")
    print("Know what you want to name your pet? Enter 1\n"
          "If not enter 2 and we'll give you a list to chose from")
    # getting the user to choose if they want to enter their own name for their pet
    # or choose from a list
    pet_name = check_int("Enter your option", "Please enter either 1 or 2", 1, 2)
    # if user wants to name them with their own name and does the function
    if pet_name == 1:
        user_enter_name()
    # if user wants to choose a name from the list and does the specific function
    else:
        chose_name()


# getting the user to set the beginning weight of their pet
def set_weight():
    # getting the user to entering the beginning weight of their pet
    print()
    weight = check_float("Enter the weight of your virtual pet to beginning "
                         "with (between 1.5 and 2.5) ", "Whoops please enter"
                                                        " a number between 1.5"
                                                        " and 2.5", 1.5, 2.5)

    # return weight to be used later outside loop
    return weight


# Function to allow user to choose a food and feed pet said food

def user_choice_food(weight):
    food_menu = []
    print("Please choose an option from the following foods:")
    number = 1
    # list foods in a for loop
    for food in FOOD_DICT:
        # print the foods in the list
        print("{}.  {}".format(number, food.title()))
        number += 1
        food_menu.append(food)

    # getting the user to enter their choice
    choice = check_int("Please choose an option from the list - type the "
                       "number >>", "Please choose a number between 1 and 5.",
                       1, 5)

    # so the name of the chosen food will print on the next line
    chosen_food = food_menu[choice - 1]

    # printing the food the pet will eat
    print("You will feed your pet {}.".format(chosen_food.title()))

    # adding the value of the food to the pets current weight
    weight += FOOD_DICT[chosen_food]

    # return weight to be used later outside loop
    return weight


# Function to allow user to choose an activity and pet do said activity
def user_choice_exercise(weight):
    activity_menu = []
    print("Please choose an option from the following activities:")

    number = 1
    # print the exercises in the list
    for activity in EXERCISE_DICT:
        print("{}.  {}".format(number, activity.title()))
        number += 1
        activity_menu.append(activity)

    choice = check_int("Please choose an option from the list - type the"
                       " number >> ", "Please choose a number between 1 "
                                      "and 5.", 1, 5)

    # so the name of the chosen food will print on the next line
    chosen_activity = activity_menu[choice - 1]

    # printing the activity the pet will do
    print("Your pet will {}.".format(chosen_activity.title()))

    # subtracting the value of the food to the pets current weight
    weight += EXERCISE_DICT[chosen_activity]

    # return weight to be used later outside loop
    return weight


# function to check if the pet's weight is too high or low
# if too high or low informs users the pet has died
def death_checker(weight):
    # if the weight is 2.6 or greater inform user, pet has died
    if weight > 2.5:
        # simple message saying the users pet has died and why
        print("You fed your pet too much and they died")
        print("Your pet weighed {:1.1f}".format(weight))

        # setting pet_alive loop to false to end game
        pet_alive = False

    # if the weight is 1.4 or lower inform user, pet has died
    elif weight < 1.5:
        # simple message saying the users pet has died and why
        print("You didn't feed your pet enough and they died.")
        print("Your pet weighed {:1.1f}".format(weight))
        # setting pet_alive loop to false to end game
        pet_alive = False

    # if pets weight is ok keep pet_alive = True and continue game
    else:
        pet_alive = True

    # return pet_alive to be used later outside loop
    return pet_alive


# food dictionary with the available foods
# along with the weight the pet will gain
FOOD_DICT = {"Carrots": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3,
             "Chocolate": 0.4}

# exercise dictionary with the available exercises to do
# along with the weight the pet will lose
EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

# list of names for the user to choose from
NAME_LIST = ["Coco", "Charlie", "Alvin", "Cupcake", "Felix", "Jazz", "Midnight", "Peanut", "Pearl", "Roxie"]


# beginning of main routine

# welcome info stating help info
welcome_info()

# formatting the title
print()
formatting("-", "Naming Your Pet")
# getting the user to select a name for their pet
user_choice_name()

# getting the user to select a weight for their pet
pet_weight = set_weight()

print()

# Setting alive loop to true
# loop for game to continue

alive = True

# while the pet is alive run the game
while alive:

    # menu for the user to choose an option
    print("-" * 20)
    print()
    formatting("*", "Menu")
    print()

    # menu for the user to choose the options from
    print("Please choose an option from the following menu:")
    print("1. Show current weight\n"
          "2. Feed Pet\n"
          "3. Exercise Pet\n"
          "4. See help information\n"
          "5. Exit\n")
    # getting the user to enter their choice.
    option = check_int("Enter your choice: ", "You must choose a number "
                                              "between 1 and 5.", 1, 5)
    # if user enters 1 print the current weight of the pet
    if option == 1:
        print("Your pet currently weighs {:1.1}".format(pet_weight))

    # if user enters 2, runs the feeding function along with checking if the pet weight is too high/low
    # causing the pet to die
    if option == 2:
        print()
        # changing the pet weight to the new pet weight
        # (increasing the weight as the pet is being feed)
        pet_weight = user_choice_food(pet_weight)
        # checking if the pet is alive depending on it's current weight
        # and setting alive to either true or false depending if the pet is dead or alive
        alive = death_checker(pet_weight)

    # if user enters 3 runs the exercise function along with checking if the pet weight is too high/low
    # causing the pet to die
    if option == 3:
        print()
        pet_weight = user_choice_exercise(pet_weight)
        # checking if the pet id alive depending on it's current weight
        # and setting alive to either true or false depending if the pet is dead or alive
        alive = death_checker(pet_weight)

    # if user enters 4 print the help information
    if option == 4:
        help_info()

    # if user enters 5, break loop and end game
    if option == 5:
        # setting alive to false so the loop stops and game finishes
        alive = False
        break

# the game ends and thanks the user for playing
print("Thanks for playing")
