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
            profit_type = "unknown"
            amount = response

        try:
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f} ie {:.2f} dollars? ".format(amount, amount))

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? ".format(amount))

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Main Routine goes here
all_costs = 200

# Loop for quick testing...
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))
    print()
