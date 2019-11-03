# printing the exercises available for the user to do to the pet
# with corresponding numbers

# exercise dictionary with the available exercises to do
# along with the weight the pet will lose
EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

number = 1
# print the exercises in the list
for activity in EXERCISE_DICT:
    print("{}.  {}".format(number, activity.title()))
    number += 1




