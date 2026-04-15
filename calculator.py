# dictionary of operations
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
operations = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
}
calculate = True
while calculate:
    while True:
    # ask user for operation
        raw = input("Enter your desired operation: ")
        try:
            operation = operations[raw]
            break
        except KeyError:
            print("Enter valid operation only!")
    while True:
        # user input 1
        num_1 = input("Enter your first number here: ")
        try:
            num_1 = float(num_1)
            break
        except ValueError:
            print("Enter numerics only!")
    while True:
        # user input 2
        num_2 = input("Enter your second number here: ")
        try:
            num_2 = float(num_2)
            break
        except ValueError:
            print("Enter numerics only!")
    try:
        total = f"{num_1} {raw} {num_2} = {operation(num_1,num_2)}"
        print(total)
    except ZeroDivisionError:
        print(f"Zero division error! {num_1} cannot be divided to {num_2}!")
    while calculate:
        proceed = input("Shall we proceed? Yes or no only: ").lower()
        match proceed:
            case "yes":
                print("\n")
                break
            case "no":
                calculate = False
            case _:
                print("Unknown response!")