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


# *** Main routine starts here ***

want_instructions = yes_no("Would you like to see the instructions? ")

# get_int = num_check("How many do you need? ", "Please enter an amount more than 0\n", int)
# get_cost = num_check("How much does it cost for each one? $", "Please enter a real price\n", float)

# Get product name
product_name = not_blank("Product name: ", "Please enter a name for your product")

# get variable expenses
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

fixed_or_no = yes_no("Do you have any fixed costs? ")

# Get fixed expenses if necessary
if fixed_or_no == "yes":
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_frame = ""
    fixed_sub = 0


# Printing area

print(variable_frame)
print("\nVariable Costs: ${:.2f}".format(variable_sub))
overall_cost = variable_sub + fixed_sub

if fixed_or_no == "yes":
    print("\n", fixed_frame[['Cost']])
    print("\nFixed Costs: ${:.2f}\n".format(fixed_sub))

print("\nOverall Costs: ${:.2f}".format(overall_cost))
