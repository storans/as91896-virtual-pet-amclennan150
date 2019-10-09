# Check if person is eligible for superannuation

# Set constant SUPER_AGE to 65 as to changes in program
SUPER_AGE = 65
# Loop to allow  testing of different versions
keep_going = ""

while keep_going == "":
    age = int(input("What is your age?"))

    # User input must be greater than or equal to 65
    if age >= SUPER_AGE:
      print("YES")
    else:
        print("no")

# Ask user if they want to continue
    keep_going = input("press enter to continue?")

print("ciao")
