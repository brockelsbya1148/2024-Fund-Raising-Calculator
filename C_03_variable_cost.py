import pandas


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


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}  \nTry again\n".format(error))
            continue

        return response


def currency(x):
    return "${:.2f}".format(x)


# *** Main routine starts here ***

# Set up dictionaries and lists

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data
product_name = not_blank("Product name: ", "Please enter a name for your product")


# loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and price
    item_name = not_blank("Item name: ", "Please enter a name for the component")
    if item_name.lower() == "xxx":
        break

    quantity = num_check("Quantity: ", "Please enter an amount more than 0", int)

    price = num_check("How much for 1? $", "Please enter a real cost", float)

    # add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculate cost of each component
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

# Find subtotal
variable_sub = variable_frame['Cost'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# *** Printing Area ****

print(variable_frame)

print()

print("Variable Cost: ${:.2f}".format(variable_sub))
