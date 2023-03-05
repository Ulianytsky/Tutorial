# Not work
result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand = float(input("Enter next num >>> "))
            if result is None:
                result = operand
            wait_for_number = False
        except ValueError:
            print(f"{operand} is not a number. Try again")
            wait_for_number = True
            continue

    if wait_for_number == False:
        operator = input("Enter operator >>> ")
        if operator in ('+', '-', '*', '/'):
            result = result + operator

# if operator == '+':
#     result += operand
#     wait_for_number = True
# elif operator == '-':
#     result -= operand
#     wait_for_number = True
# elif operator == '*':
#     result *= operand
#     wait_for_number = True
# elif operator == '/':
#     try:
#         result /= operand
#     except ZeroDivisionError:
#         print("ZeroDivision Enter another number")
#         wait_for_number = True
    #     continue
    # elif operator == '=':
    #     print(result)
    #     break
    # else:
    #     print(f"{operator} is not '+' or '-' or '*' or '/'")
    #     continue
# # В тебе result += operand виконується коли перший operand
# # вже присвоений в result  тобто 10+5 в тебе виконується як 10+10
