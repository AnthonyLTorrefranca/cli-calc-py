def add(n1, n2):
    print("This is addition")
    return n1 + n2
def subtract(n1, n2):
    print("This is subtraction")
    return n1 - n2
def multiply(n1, n2):
    print("This is multiplication")
    return n1 * n2
def division(n1, n2):
    print("This is division")
    return n1 / n2

operands = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}
print("""
Welcome to CLI Calculator here is a list of operand this calculator can work: 
+ for addition
- for subtraction
* for multiplication
/ for division
""")

def operand():
    operando = input("Enter an operand to the given actions: ")
    return operando

# get the first number
number_1 = int(input("Enter the first number: "))

# check if the chosen operand exists in the dictionary
while True:
    # get what the user want to operand to execute
    chosen = operand()
    if chosen in operands:
        print(chosen)
        break
    if chosen not in operands:
        print("Nah uh")


# get the second number
number_2 = int(input("Enter the second number: "))



# call the function using the dictionary and the two numbers
# store and print the final calculation
# prevent the program from crashing on math errors (like dividing by zero)
# wrap everything so the user can perform another calculation without restarting