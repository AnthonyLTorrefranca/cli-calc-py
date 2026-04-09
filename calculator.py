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
        raw_sign = input("Input operation here: ")
        try:
            operation = operations[raw_sign]
            break
        except KeyError:
            print("Nah uh")

    while True:
        num_1 = input("Enter your first number here: ")
        try:
            num_1 = float(num_1)
            break
        except ValueError:
            print("Nah uh")

    while True:
        num_2 = input("Enter your second number here: ")
        try:
            num_2 = float(num_2)
            break
        except ValueError:
            print("Nah uh")

    total = f"{num_1} {raw_sign} {num_2} = {operation(num_1,num_2)} "
    print(total)

    while True:
        proceed = input("Shall we proceed? yes or no: ").lower()
        if proceed == "y":
            print("Let's go!")
        elif proceed == "yes":
            print("Let's go!")
        elif proceed == "n":
            print("Bye!")
            break
        elif proceed == "no":
            print("Bye!")
            break

    calculate = False