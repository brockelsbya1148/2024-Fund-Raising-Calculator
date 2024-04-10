# Import libraries
import pandas
import math


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
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes or no\n")
            continue


# Checks that string response is not blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}  \nTry again\n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays instructions / information
def instructions():

    statement_generator("Instructions", "=")
    print("Instructions go here\n")

    return ""


# Gets expenses, returns list which has
# the data frame and subtotal
def get_expenses(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and price
        if var_fixed == "variable":
            item_name = not_blank("Name of Variable Cost: ", "Please enter a name for the component")
        else:
            item_name = not_blank("Name of Fixed Cost: ", "Please enter a name for the component")

        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "Please enter an amount more than 0", int)

        else:
            quantity = 1

        price = num_check("How much? $", "Please enter a real cost", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find subtotal
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


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
            dollar_type = yes_no("Do you mean ${:.2f}? ".format(amount, amount))

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


# rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


# *** Main routine starts here ***

want_instructions = yes_no("Would you like to see the instructions? ")

if want_instructions == "yes":
    instructions()
else:
    pass

# Get product name
product_name = not_blank("Product name: ", "Please enter a name for your product")
how_many = num_check("How many of these will you be making? ", "Must be a whole number more than 0", int)

fixed_or_no = yes_no("Do you have any fixed costs? ")

# Get fixed expenses if necessary
if fixed_or_no == "yes":
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_frame = ""
    fixed_sub = 0

# get variable expenses
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# work out total costs and profit target
overall_cost = variable_sub + fixed_sub
profit_target = profit_goal(overall_cost)

# calculate total sales needed
sales_needed = overall_cost + profit_target

# ask user for rounding
round_to = num_check("Round to nearest...? $", "More than 0", int)

# calculate recommended price
selling_price = sales_needed / how_many
rounded = round_up(selling_price, round_to)

# Printing area
statement_generator("Fund Raising - {}".format(product_name), "*")

print("-- Variable Costs --\n")
print(variable_frame)
print("\nVariable Costs: ${:.2f}\n".format(variable_sub))


if fixed_or_no == "yes":
    print("-- Fixed Costs --\n")
    print(fixed_frame[['Cost']])
    print("\nFixed Costs: ${:.2f}".format(fixed_sub))

print("\n**** Overall Costs: ${:.2f} ****".format(overall_cost))

statement_generator("Profit & Sales Targets", "-")
print("Profit Target: ${:.2f}".format(profit_target))
print("Total Sales: ${:.2f}".format(overall_cost + profit_target))

statement_generator("Pricing", "*")
print("Minimum Price: ${:.2f}".format(selling_price))
print("Recommended Price: ${:.2f}".format(rounded))
