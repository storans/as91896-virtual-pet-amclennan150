# the final component of the name section

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


# Getting the user to enter their own name for their pet
def user_enter_name():
    name_pet = input("What would you like to name your pet? >> ").title().strip()

    # if user pushes enter then automatically assigns a name
    if name_pet == "":
        name_pet = "Jazzy"
        print("You didn't name your pet, so your pet is now called {}".format(name_pet))
    else:
        # printing the chosen name
        print("Your pets name is {}".format(name_pet))

        # if user enters a name that is already in the list informs user and doesn't re add it
        if name_pet in name_list:
            print("This name is already in the list")
        else:
            add_name = ""
            while add_name is "":
                # adding name to list of names
                add_name = input(
                    "Do you want to add this name to the list of preset names? (Yes or No)").strip().lower()
                name_list.append(name_pet)
    # return pets name so can be accessed later
    return name_pet


# function for the user to chooses to name their pet one of the already
# decided names
def chose_name():
    name_option = []
    print("Choose one of the following names:")
    number = 1
    # list foods in a for loop
    for names in name_list:
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


# giving the user the option to either enter their own name for their pet
# or choose from a given list
def user_choice_name():
    print("")
    print("Know what you want to name your pet? Enter 1\n"
          "If not enter 2 and we'll give you a list to chose from")
    # getting the user to choose if they want to enter their own name for their pet
    # or choose from a list
    pet_name = check_int("Enter your option", "Please enter either 1 or 2", 1, 2)
    # if user wants to name them with their own name and does the function
    if pet_name == 1:
        user_enter_name()
    # if user wants to choose name from the list and does the specific function
    else:
        chose_name()


# list of names for the user to choose from
name_list = ["Coco", "Charlie", "Alvin", "Cupcake", "Felix", "Jazz", "Midnight", "Peanut", "Pearl", "Roxie"]

user_choice_name()
print(name_list)
