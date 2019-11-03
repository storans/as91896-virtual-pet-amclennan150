# 2d list to show which sports are available to be chosen

# 2d list with the available foods
# along with the weight the pet will gain
FOOD_LIST = [["Carrot", 0.2], ["Grass", 0.4], ["Celery", 0.1], [ "Spinach", 0.3]]

# Function to allow user to choose a sport and enter data

print("Please choose an option from the following foods:")
number = 1
for food in FOOD_LIST:
    print("{}.  {}".format(number, food))
    number += 1



