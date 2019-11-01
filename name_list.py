# giving the user the option to choose their pets name from a list


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


# function for the user to chooses to name their pet one of the names
# from the list
def chose_name():
    name_option = []
    print("Choose one of the following names:")
    number = 1
    # list foods in a for loop
    for names in NAME_LIST:
        # print the names in the list
        print("{}.  {}".format(number, names.title()))
        number += 1
        name_option.append(names)

    # getting the user to enter the number that corresponds to the name they want to pick
    chosen_name = check_int("Please choose an option from the list - type the "
                            "number >>", "Please choose a number between 1 and 5.",
                            1, 5)

    # so the name of the pet will print on the next line
    name_pet = name_option[chosen_name - 1]

    # printing the chosen name
    print("Your pets name is {}".format(name_pet))

    # return pets name so can be accessed later
    return name_pet


# list of names for the user to choose from
NAME_LIST = ["Coco", "Charlie", "Alvin", "Cupcake", "Felix", "Jazz"]


# running the function for the user to choose their pets name from a list
chose_name()

