
# Function to
def check_int(question, error, low, high): # Question and error allow it to be used in a range of situations
    valid = False

    while not valid:
        number = input("{} >> ".format(question)) # Any question that needs a whole number for the input
        try:
            number = int(number)
            if low <= number <= high:
                return number # Note, I do not set valid to True, as returning does this
            else:
                print(error)
        except ValueError:
            print(error)


# menu for the user to choose an option

print()
print("-" * 20)
print()
print("Please choose an option from the following menu:")
print("1. Show current weight\n"
    "2. Feed Pet\n"
    "3. Exercise Pet\n"
    "4. See help information\n"
    "5. Exit\n")
option = check_int("Enter your choice: ", "You must choose a number between 1 and 5.", 1, 5)

if option == 1:
    print("Show current weight")

if option == 2:
    print("Feed Pet")

if option == 3:
    print("Exercise Pet")

if option == 4:
    print("Help Information")

if option == 5:
    print("End Game")
