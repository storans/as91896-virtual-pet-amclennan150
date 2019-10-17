# Setting an initial weight for the pet
# initial_weight = 2

# Function for showing pet weight
# Function to allow user to choose a food and feed pet said food
def user_choice_food():
    initial_weight = 2
    low = 1
    high = len(FOOD_DICT)
    food_menu = []
    print("Please choose an option from the following foods:")

    number = 1
    for food in FOOD_DICT:
        print("{}.  {}".format(number, food.title()))
        number += 1
        food_menu.append(food)

    choice = int(input("Please choose an option from the list - type the number >> ", ))
    # "Please choose a number between {} and {}.".format(low, high), low, high)

    chosen_food = food_menu[choice - 1]

    print("You will feed your pet {}.".format(chosen_food.title()))

    initial_weight += FOOD_DICT[chosen_food] + 0


    print("Your pets current weight is {}".format(initial_weight))

FOOD_DICT = {"Carrots": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3, "Chocolate": 0.4}

user_choice_food()


