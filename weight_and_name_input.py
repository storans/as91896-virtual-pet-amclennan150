# allows user to enter the starting weight of their virtual Pet and name pet


# function to check the user has inputted a float
def check_float(question, error, low, high):  # Question and error allow it to be used for various questions
    valid = False

    while not valid:
        number = input("{} >> ".format(question))  # Any question that needs a number as the input
        try:
            number = float(number)
            if low <= number <= high:
                return number
            else:
                print(error)  # if the user enters un invalid number
        except ValueError:
            print(error)


# Getting the user to name their pet
name = input("What would you like to name your pet? >> ")

# Getting the user to input their virtual pets starting weight by running through the function
initial_weight = check_float("Enter the weight of your virtual pet to beginning with (between 1.5 and 2.5) ",
                             "Whoops please enter a number between 1.5 and 2.5", 1.5, 2.5)


# Printing the users input
print("The beginning weight of {} is {}.".format(name, initial_weight))
