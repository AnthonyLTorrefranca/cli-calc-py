# dictionary of operations
operations = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
}
# List of operations that will work
print("""
Welcome to the CLI Calculator
where we calculate things up,
The following is the corresponding operations,
'+' for addition,
'-' for subtraction, 
'*' for multiplication,
 and for  '/' division.
""")
# calculator handler
calculate = True
while calculate:
    # ask user for operation
    while True:
        raw_sign = input("Enter your desired operation: ")
        try:
            operation = operations[raw_sign]
            break
        except KeyError:
            print("Pls enter valid operation!")
    # user input 1
    while True:
        num_1 = input("Enter first number here: ")
        try:
            num_1 = float(num_1)
            break
        except ValueError:
            print("Enter numerics only!")
    # user input 2
    while True:
        num_2 = input("Enter second number here: ")
        try:
            num_2 = float(num_2)
            break
        except ValueError:
            print("Enter numerics only!")
    try:
        total = f"{num_1} {raw_sign} {num_2} = {operation(num_1, num_2)} "
        print(total)
    except ZeroDivisionError:
        print(f"{num_1} not divisible by {num_2}")
    while calculate:
        proceed = input("Shall we proceed? yes or no ").lower()
        match proceed:
            case "yes":
                break
            case "no":
                calculate = False
            case _:
                print("Unknown response!")