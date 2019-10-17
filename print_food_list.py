# Function to show which sports are available to be chosen
def show_food():
    number = 1
    for food in FOOD_DICT:
        print("{}.  {}".format(number, food.title()))
        number += 1


FOOD_DICT = {"Carrot": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3, "Chocolate": 0.4}

# printing the function to check it works
show_food()
