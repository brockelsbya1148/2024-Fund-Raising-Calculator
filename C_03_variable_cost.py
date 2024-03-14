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


def name_input(question):

    while True:

        response = input(question).strip()

        if response == "":
            print("Please enter a name\n")
        else:
            return response


while True:
    item_name = name_input("What is the name of your item? ")
    print("Item name: {}\n".format(item_name))

    component_name = name_input("What is the name of your component? ")
    print("The name of your component is {}\n".format(component_name))

    how_many = num_check("How many do you need? ", "Please enter an amount more than 0\n", int)
    print("You are making {} {}\n".format(how_many, component_name))

    component_cost = num_check("What is the cost of your component? $", "Please enter a real price\n", float)
    print("Your component ({}) costs ${:.2f}\n".format(component_name, component_cost))

    component_subtotal = component_cost * how_many
    print("The subtotal of your component ({}) is ${:.2f}\n".format(component_name, component_subtotal))
