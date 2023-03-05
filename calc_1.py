result = None
operand = None
operator = None
wait_for_number = True


while True:
    operand = input("Enter the number: ")
    if wait_for_number:

        try:
            operand = float(operand)
            wait_for_number = False

        except ValueError:
            print(f"{operand} is not a number")
            continue
        if result == None:
            result = operand
            print(result)
        else:
            result = str(eval(result+operand))
            print(result)
    else:
        if operator in ('+', '-', '*', '/'):
            operator = input("Enter '+', '-', '*', '/': ")
            wait_for_number = True

        elif operator in ['+', '-', '*', '/']:
            result = result + operator
            wait_for_number = True
        elif operator == "=":
            result = int(float(result))
            print(result)
            break

        else:
            print('invalid operator')
