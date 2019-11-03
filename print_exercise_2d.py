# printing the exercises available for the user to do to the pet
# with corresponding numbers

# exercise dictionary with the available exercises to do
# along with the weight the pet will lose
EXERCISE_LIST = [["Hop", -0.2], ["Walk", -0.4], ["Run", -0.1], ["Jump", -0.3]]

# food dictionary with values of weight to be added
number = 1

# print the exercises in the list
for activity in EXERCISE_LIST:
    print("{}.  {}".format(number, activity))
    number += 1



