# getting the pet to die (only decreasing weight)
# only underweight is needed as only testing with exercise here


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

    choice = int(input("Please choose an option from the list - type the"
                       " number >>"))

    # so the name of the chosen food will print on the next line
    chosen_activity = activity_menu[choice - 1]

    # printing the activity the pet will do
    print("Your pet will {}.".format(chosen_activity.title()))

    # subtracting the value of the food to the pets current weight
    weight += EXERCISE_DICT[chosen_activity]

    # return weight to be used later outside loop
    return weight


def death_checker(weight):
    # if the weight is 2.6 or greater inform user, pet has died
    # only underweight is needed as only testing with exercise here
    if weight < 1.5:
        # simple message saying the users pet has died and why
        print()
        print("You exercised your pet too much and they died")
        print("Your pet weighed {:1.1f}kgs".format(weight))

        # setting pet_alive loop to false to end game
        pet_alive = False

    # if pets weight is ok keep pet_alive = True and continue game
    else:
        pet_alive = True

    # return pet_alive to be used later outside loop
    return pet_alive


# exercise dictionary with the available exercises to do
# along with the weight the pet will lose
EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

# setting weight to 2 for testing
pet_weight = 2

# Setting alive loop to true
# loop for game to continue
alive = True

# while the pet is alive run the game
while alive:
    # changing the pet weight to the new pet weight
    # (increasing the weight as the pet is being feed)
    pet_weight = user_choice_exercise(pet_weight)
    # checking if the pet is alive depending on it's current weight
    # and setting alive to either true or false depending if the pet is dead or alive
    alive = death_checker(pet_weight)

# if pet dies thank user for playing
print("Thanks for playing")
