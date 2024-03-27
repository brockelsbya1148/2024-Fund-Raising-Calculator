# functions go here


# Checks that user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes or no\n")
            continue


def profit_goal(total_costs):

    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        response = input("What is your profit goal? (eg $500 or 50%) ")

        if response[0] == "$":
            profit_type = "$"
            amount = response[1:]

        elif response[-1] == "%":
            profit_type = "%"
            amount = response[:-1]

        else:
            if response <= 100:
                percent_or_dollar = yes_no("Did you mean {}%? ")
                if percent_or_dollar == "yes":
                    profit_type = "%"
                else:
                    profit_type = "$"
            else:
                percent_or_dollar = yes_no("Did you mean ${:.2f}? ")
                if percent_or_dollar == "yes":
                    profit_type = "$"
                else:
                    profit_type = "%"


# Main Routine goes here
all_costs = 200

# Loop for quick testing...
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))
    print()
