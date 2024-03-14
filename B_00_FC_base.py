# Import libraries
import pandas


# **** Functions go here ****

# Checks that input is either a float or an integer that is more than zero
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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


# Main routine goes here
want_instructions = yes_no("Would you like to see the instructions? ")

get_int = num_check("How many do you need? ", "Please enter an amount more than 0\n", int)
get_cost = num_check("How much does it cost for each one? $", "Please enter a real price\n", float)
