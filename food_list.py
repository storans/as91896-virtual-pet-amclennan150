# Function to show which sports are available to be chosen
def show_food():
    number = 1
    for food in FOOD_DICT:
        print("{}.  {}".format(number, food.title()))
        number += 1


# Function to allow user to choose a sport and enter data
def user_choice():
    food_menu = []
    print("Please choose an option from the following foods:")

    number = 1
    for food in FOOD_DICT:
        print("{}.  {}".format(number, food.title()))
        number += 1
        food_menu.append(food)
    # Getting the user to choose an option from the list of foods
    choice = int(input("Please choose an option from the list - type the number >> "))

    chosen_food = food_menu[choice - 1]

    # printing the users choice along with context
    print("You will feed your pet {}.".format(chosen_food.title()))


FOOD_DICT = {"Carrot": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3}
user_choice()
