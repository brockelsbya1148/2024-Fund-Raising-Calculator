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


while True:
    ask = yes_no("Yes or No? ")
