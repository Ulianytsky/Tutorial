result = None
operand = None
operator = None
wait_for_number = True
while True:
    user_input = input('>>> ')
    if wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print(f"{operand} is not a number. Try again.")
    else:
        operator = user_input
        if operator in ('+', '-', '*', '/'):
            if operator == '+':
                result += operand
                wait_for_number = True
            elif operator == '-':
                result -= operand
                wait_for_number = True
            elif operator == '*':
                result *= operand
                wait_for_number = True
            elif operator == '/':
                try:
                    result /= operand
                except ZeroDivisionError:
                    print('You can not divide by zero. Try again')
                    wait_for_number = True
                    continue
            else:
                print('Your operator is not '+' or ' -
                      ' or '*' or '/'. Try again.')
                wait_for_number = True
                continue
    if user_input == '=':
        print(result)
        break
