import art

print(art.logo)

result = None

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        print("Please enter non zero for denominator")
        return None
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculation(n1,oper, n2):
    global result
    if oper == "+":
        result = operations["+"](n1, n2)
        print(f"{n1} {oper} {n2} = {result}")
    elif oper == "-":
        result = operations["-"](n1, n2)
        print(f"{n1} {oper} {n2} = {result}")
    elif oper == "*":
        result = operations["*"](n1, n2)
        print(f"{n1} {oper} {n2} = {result}")
    elif oper == "/":
        result = operations["/"](n1, n2)
        print(f"{n1} {oper} {n2} = {result}")
    else:
        print("Enter a valid operator")
        return None

should_continue = ""

while True:
    num_1 = float(input("Enter first number: "))
    for symbols in operations:
        print(symbols)
    operator = input("Enter a operator: ")
    num_2 = float(input("Enter second number: "))
    check = calculation(num_1, operator, num_2)
    if check == None:
        continue
    while True:
        should_continue = input("Enter 'y' to continue with operation or 'n' to start new calculation or 'e' to exit: ")

        if should_continue == "y":
            num_1 = result
            print(f"number 1 is {result}")
            while True:
                operator = input("+ \n- \n* \n/ \nEnter an operator: ")
                if operator in ["+", "-", "*", "/"]:
                    break
                else:
                    print("Invalid operator! Please enter a valid operator.")
            num_2 = float(input("Please enter number 2: "))
            calculation(num_1, operator, num_2)
        elif should_continue == "n":
            print("Starting a new calculation....")
            break
        elif should_continue == "e":
            print("Exiting calculator. Goodbye!")
            exit()
        else:
            print("Please enter a valid input")

