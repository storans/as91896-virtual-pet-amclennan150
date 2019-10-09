SUPER_AGE = 65
keep_going = ""

while keep_going == "":
    age = int(input("What is your age?"))

    if age >= SUPER_AGE:
      print("YES")
    else:
        print("no")

    keep_going = input("press enter to continue?")

print("ciao")
