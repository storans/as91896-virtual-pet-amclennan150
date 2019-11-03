# printing the exercises in the exercise dictionary using a dictionary

# exercise dictionary with the available exercises to do
# along with the weight the pet will lose
EXERCISE_DICT = {"Hop": -0.2, "Walk": -0.4, "Run": -0.1, "Jump": -0.3}

# setting number to one so the foods will print with the correct number
number = 1
# show which sports are available to be chosen
for activity in EXERCISE_DICT:
    print("{}.  {}".format(number, activity.title()))
    number += 1







