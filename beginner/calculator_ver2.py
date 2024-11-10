def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# using dict to store func as values
operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
def calculate():
    do_accumulate = True
    num1 = float(input("Enter the first number: "))

    while do_accumulate:
        for signs in operators.keys():
            print(signs)
        choices = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))
        result = operators[choices](num1, num2)

        print(f"{num1} {choices} {num2} = {result}")

        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if continue_calculating == 'y':
            num1 = result
        else:
            do_accumulate = False
            calculate()

calculate()
