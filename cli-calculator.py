print("Welcome to the CLI Calculator\nWhere I'll be getting the operation on what to create coming from you\nTwo numbers after it!")

operations = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b,
}

def operation():
    while True:
        operand = input("Enter your dedicated operand +, -, *, and / only: ")
        try:
            operate = operations[operand]
            break
        except KeyError:
            print("Nope, not an acceptable operand!")
    while True:
        num_1 = input("Enter your first number here: ")
        try:
            num_1 = int(num_1)
            break
        except ValueError:
            print("Nah uh numerics only")
    while True:
        num_2 = input("Enter your second number here: ")
        try:
            num_2 = int(num_2)
            break
        except ValueError:
            print("Nah uh numerics only")

    # zero division handler
    try:
        calculate = f"{num_1} {operand} {num_2} = {operate(num_1, num_2)}"
        print(calculate)
    except ZeroDivisionError:
        print("Cannot be divided to zero!")

def proceed():
    shall = input("Shall we proceed, Yes or no? ").lower()
    while True:
        match shall:
            case "y" | "ye" | "yes" | "yah" :
                calculate = True
                break
            case "n" | "no" | "nah" | "nope" :
                print("See yah🫡")
                calculate = False
                break
    return calculate
calculate = True
while calculate:
    operation()
    calculate = proceed()