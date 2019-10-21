# welcome user to program

# function for formatting the title
def formatter(character, output):
    print(character * (len(output) + 5))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 5))


# print welcoming message along with how the game works
print("Welcome to your own virtual pet!\n"
      "You will be able to choose your pets name along with their beginning weight\n"
      "For your pet to survive it must be kept between a weight of 1.5kg and 2.5kg, don't worry we'll tell you if your pet is near these")
