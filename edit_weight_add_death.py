# Function for showing and changing pet weight

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
    choice = int(input("Please choose an option from the list - type the "
                       "number >>"))

    # so the name of the chosen food will print on the next line
    chosen_food = food_menu[choice - 1]

    # printing the food the pet will eat
    print("You will feed your pet {}.".format(chosen_food.title()))

    # adding the value of the food to the pets current weight
    weight += FOOD_DICT[chosen_food]

    # return weight to be used later outside loop
    return weight


def set_weight():
    initial_weight = float(input("Please enter a weight"))
    return initial_weight


def death_checker(weight):
    # if the weight is 2.6 or greater inform user, pet has died
    # only overweight is needed as only testing with food here
    if weight > 2.6:
        # simple message saying the users pet has died and why
        print("You fed your pet too much and they died")
        print("Your pet weighed {}".format(weight))

        # setting pet_alive loop to false to end game
        pet_alive = False

    # if pets weight is ok keep pet_alive = True and continue game
    else:
        pet_alive = True

    # return pet_alive to be used later outside loop
    return pet_alive


FOOD_DICT = {"Carrots": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3, "Chocolate": 0.4}

# setting weight to 2 for testing
pet_weight = 2

# Setting alive loop to true
# loop for game to continue
alive = True

# while the pet is alive run the game
while alive:
    # changing the pet weight to the new pet weight
    # (increasing the weight as the pet is being feed)
    pet_weight = user_choice_food(pet_weight)
    # checking if the pet is alive depending on it's current weight
    # and setting alive to either true or false depending if the pet is dead or alive
    alive = death_checker(pet_weight)

# if pet dies thank user for playing
print("Thanks for playing")
