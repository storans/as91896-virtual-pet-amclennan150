if __name__ == "__main__":
    sports_dict = {"run": 3, "swim": 3, "walk": 1, "cycle": 2, "yoga": 1}
    user_goal = None
    total_exercise = None
    # First is a variable set to True to check whether the program should continue running.

    print("Fitness Tracker")

    tracking_on = True
    while tracking_on == True:

        # Start an infinite loop to prompt for a correct option value
        while True:
        # Create an option variable to store the user's chosen option.

            test = int(input("please enter a number"))

            if test == 1:
                print("Yay")

            if test == 2:
                tracking_on = False
            break

    print("Fare thee well.")
