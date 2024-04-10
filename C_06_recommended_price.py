import math


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


# rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


# Main routine
item_amount = num_check("How many items? ", "Please enter a whole number that is more than 0", int)
total_cost = num_check("Total Costs? ", "More than 0", float)
profit_goal = num_check("Profit Goal? ", "More than 0", float)
round_to = num_check("Round to nearest...? ", "Please enter a whole number that is more than 0", int)

print("Total: ${:.2f}".format(total_cost))
print("Profit Goal: ${:.2f}".format(profit_goal))

sales_needed = total_cost + profit_goal
selling_price = sales_needed / item_amount
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

rounded = round_up(selling_price, round_to)
print("${:.2f} --> ${:.2f}".format(selling_price, rounded))
