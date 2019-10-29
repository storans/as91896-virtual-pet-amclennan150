# Function for showing and changing pet weight

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
    initial_weight = 2  # SEtting initial weight for pet
    low = 1
    high = 5

    food_menu = []
    print("Please choose an option from the following foods:")

    number = 1
    for food in FOOD_DICT:
        print("{}.  {}".format(number, food.title()))
        number += 1
        food_menu.append(food)

    choice = check_int("Please choose an option from the list - type the number >> ",
     "Please choose a number between 1 and 5.", low, high)

    chosen_food = food_menu[choice - 1]

    #print("You will feed your pet {}.".format(chosen_food.title()))

    initial_weight += FOOD_DICT[chosen_food]

    print("Your pets current weight is {}".format(initial_weight))

    return initial_weight

FOOD_DICT = {"Carrots": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3, "Chocolate": 0.4}
a = True
while a is True:
    choice = int(input("1 or 2"))

    if choice == 1:
        user_choice_food()

    if choice == 2:
        break
