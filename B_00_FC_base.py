# Import libraries


# **** Functions go here ****

# Checks that input is either a float or an integer that is more than zero
def num_check(question):

    while True:

        try:
            response = int and float(input(question))
            if response <= 0:
                print("Please enter a number that is more than 0")
                continue
            return response

        except ValueError:
            print("Please enter an integer")


while True:

    number = num_check("Number: ")
