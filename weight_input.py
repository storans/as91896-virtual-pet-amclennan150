# allow user to enter the starting weight of their Virtual Pet

def check_float(question, error, low, high):  # Question and error allow it to be used in a range of situations
    valid = False

    while not valid:
        number = input("{} >> ".format(question))  # Any question that needs a number as the input
        try:
            number = float(number)
            if low <= number <= high:
                return number
        except ValueError:
            print(error)


# Getting the user to input their virtual pets starting weight by running through the function
initial_weight = check_float("Enter the weight of your virtual pet to beginning with (between 1.5 and 2.5) ",
                             "Whoops please enter a number between 15 and 2.5", 1.5, 2.5)

# Printing the users input with context
print("The beginning weight is {}.".format(initial_weight))
