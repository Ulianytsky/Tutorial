result = None
operand = None
operator = None
wait_for_number = True
while True:
    if wait_for_number == True:
        operand = input("Enter the numebr: ")
        try:
            number = float(operand)
            wait_for_number = False
        except ValueError:
            print(f"{operand} not number ")
            continue
        if result == None:
            result = operand
        else:
            result = eval(result + operand)
            result = str(result)
    else:
        operator = input("Enter operator: ")
        if operator in ("+", "-", "*", "/"):
            result += operator
            wait_for_number = True
        elif operator == "=":
            result = int(float(result))
            break
        else:
            print(f"{operator} not operator")
