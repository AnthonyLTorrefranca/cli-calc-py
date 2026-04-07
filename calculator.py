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

calculate = True

def operand():
    operando = input("Enter an operand to the given actions: ")
    return operando

def calculated(number_1, chosen, number_2):
    # variable for total calculations
    match chosen:
        case "+":
            total_calculated = number_1 + number_2
            print(f"{number_1} {chosen} {number_2}= {total_calculated}")
        case "-":
            total_calculated = number_1 - number_2
            print(f"{number_1} {chosen} {number_2}= {total_calculated}")
        case "*":
            total_calculated = number_1 * number_2
            print(f"{number_1} {chosen} {number_2}= {total_calculated}")
        case "/":
            total_calculated = number_1 / number_2
            print(f"{number_1} {chosen} {number_2}= {total_calculated}")


num_1=""
num_2=""
chosen=""

while calculate:
    while True:
        # get the first number
        num_1 = input("Insert first number here: ")
        try:
            num_1 = float(num_1)
            break
        except ValueError:
            print("Please enter numerical only!")

    while True:
        # get what the user want to operand to execute
        chosen = operand()
        # check if the chosen operand exists in the dictionary
        if chosen in operands:
            break
        else:
            print("Nah uh")

    while True:
        num_2 = input("Insert the second number: ")
        try:
            num_2 = float(num_2)
            calculated(num_1, chosen, num_2)
            break
        except ValueError:
            print("Please enter numerical only!")


    shall = True
    proceed = input("Shall we continue? Yes or no: ").lower()
    while shall:
        match proceed:
            case "yes":
                calculate = True
                break
            case "no":
                calculate = False
                break
            case _:
                print("Not on the list!")
                proceed = input("Shall we continue? Yes or no: ").lower()

