# Import libraries


# **** Functions go here ****

# Checks that input is either a float or an integer that is more than zero
def num_check(question):

    while True:

        try:
            response = int and float(input(question))
            if response <= 0:
                print("Please enter a number that is more than 0\n")
                continue
            return response

        except ValueError:
            print("Please enter an integer\n")


# Checks that input is either yes or no (or shortened to y/n)
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print("You said yes\n")
            return "yes"

        elif response == "no" or response == "n":
            print("You said no\n")
            return "no"

        else:
            print("Please answer yes or no\n")
            continue


# Loop for testing
while True:

    number = num_check("Number: ")
    print()

    yes_or_no = yes_no("Yes or No? ")
