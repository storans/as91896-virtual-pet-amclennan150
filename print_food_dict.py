# printing the food in the food dictionary

# food dictionary with values of weight to be added
FOOD_DICT = {"Carrot": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3}

# setting number to one so the foods will print with the correct number
number = 1

# printing the food dictionary in a list with numbers
for food in FOOD_DICT:
    print("{}.  {}".format(number, food.title()))
    number += 1
