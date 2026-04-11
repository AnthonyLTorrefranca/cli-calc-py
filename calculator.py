# dictionary for operation
operations = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
}
# instruction display
print("""
Welcome to CLI Calculator here is a list of operand this calculator can work:
+ for addition
- for subtraction
* for multiplication
/ for division
""")
# start of the calculator
calculate = True
while calculate:
    while True:
        try:
            raw_sign = input("Enter valid operation here: ")
            operation = operations[raw_sign]
            break
        except KeyError:
            print("Enter valid operation!")
    # first number here
    while True:
        try:
            num_1 = input("Input your first number here: ")
            num_1 = float(num_1)
            break
        except ValueError:
            print("Enter numerics only!")
    # second number here
    while True:
        try:
            f_num_2 = input("Input your second number here: ")
            num_2 = float(f_num_2)
            break
        except ValueError:
            print("Enter numerics only!")
    # zero division handler
    try:
        total = f"{num_1} {raw_sign} {num_2} = {operation(num_1, num_2)}"
        print(total)
    except ZeroDivisionError:
        print(f"{num_1} cannot be divided to {f_num_2}\n")
    # asks if the user wants to proceed
    while calculate:
        proceed = input("Shall we proceed? yes or no ")
        match proceed:
            case "yes":
                break
            case "no":
                calculate = False
                break
            case _:
                print("Unknown response!")









