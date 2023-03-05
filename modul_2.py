# exercise 1
''' На техническом собеседовании претенденты на 
должность получают оценку за тест. В следующий тур 
собеседования проходят кандидаты, сдавшие тест на 83 балла включительно или выше. 
Реализуйте оператор контроля выполнения так, чтобы он присвоил логической переменной is_next 
значение True, если количество набранных баллов будет больше или равно 83. 
В противном случае значение переменной равно False.'''

# is_next = True
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next

# else:
#     is_next = False
# print(is_next)

# exercise 2
'''У нас есть три логические переменные.

Первая определяет статус пользователя is_active, которая равна True или False.
Вторая is_admin определяет, есть ли у пользователя права администратора, булевого типа.
Третья is_permission — разрешен ли доступ, тоже булевого типа.
Приведите переменные is_active, is_admin и is_permission к булевому виду.

Присвойте переменной access, значение, которое покажет, есть ли доступ у пользователя. 
Используйте логические операторы.

Администратор всегда имеет доступ, независимо от значений переменных is_permission и is_active.

Пользователь имеет доступ, только если is_permission равен True и is_active также равен True'''

# is_active = input("Is the user active? ")
# is_admin = input("Is the user administrator? ")
# is_permission = input("Does the user have access? ")

# is_active = True
# is_admin = True
# is_permission = True


# access = print(access)

# exercise 3

'''Как известно, обычно разработчиков принято делить на три категории: 
Джун (Junior) — младший специалист, Мидл ( Middle) — основной разработчик в 
компании и Сеньйор (Senior) — старший разработчик. 
Ориентировочно можно считать, что до 1 года работы включительно — это Джуниор, 
больше 5 лет — это Сеньйор разработчик, а с одного года до 5 включительно — мидл.

Есть переменная work_experience, определяющая стаж работы программиста. 
В зависимости от стажа работы, присвоить переменной developer_type значение "Junior", "Middle" или "Senior".
 Используйте, если необходимо, булевы операторы ** or** и and при проверке.'''

# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience > 1 and work_experience <=5:
#     developer_type = "Middle"

# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(developer_type)


# exercise 4

'''Перепишите пример из теории, но для положительного числа проверяйте — четное оно или нет. 
Таки образом после проверок переменная result должна содержать одно из четырех значений:

"Positive even number"
"Positive odd number"
"Negative number"
"It is zero"
Подсказка: проверка на четность выполняется сравнением остатка от деления на 2 с 0 или 1. 
Напомним, остаток от деления можно получить после операции %'''

# num = int(input("Enter a number: "))

# if num > 0:
#     if num >= 100:
#         result = "Positive odd number"
#     if num % 2:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(result)


# exercise 5  (chek)

'''Вернемся к задаче расчета корней квадратного уравнения с предыдущего модуля.

Необходимо вычислить корни квадратного уравнения.

a · x2 + b · x + c = 0

Дискриминант уравнения поместите в переменную D

D = b2 - 4 · a · c

Корни уравнения поместите в переменные x1 и x2

x1 = (-b + D0.5) / (2 · a)

x2 = (-b - D0.5) / (2 · a)

В прошлый раз мы строго указали значения коэффициентов a, b, c. 
Теперь, когда мы уже знаем про ветвление, мы можем проверять значение дискриминанта и, 
в зависимости от того положительный он или отрицательный, проводить расчет корней. 
Выполните расчет корней для произвольных значений коэффициентов a, b, c.'''

# import math

# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c


# if D > 0:
#     x1 = (- b + D ** 0.5) / (2 * a)
#     x2 = (- b - D ** 0.5) / (2 * a)
#     result = x2

# exercise 6 (при кратности 2 получается 0, а значение 0 это False)

'''Выполните задание, для определения четное число или нет, с помощью тернарного оператора.

Программа устанавливает значение переменной is_even в True или False, в зависимости от того, 
является ли число в переменной num четным или нечетным.

Подсказка: проверка на четность выполняется сравнением остатка от деления на 2 с 0 или 1. 
Напомним, остаток от деления можно получить после операции %'''

# num = int(input("Enter an integer number: "))

# is_even =  True if num % 2 else False
# print(is_even)

# exercise 7 (не до конца понятно c += и i)

# n = int(input("Enter the integer (0 to 100): "))
# result = 0
# i = 0
# while i <= n:
#     result += i
#     i += 1
# print(result)


# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# i = 0
# while i <= num:
#     sum += i
#     i += 1
# print(sum)

# exercise 8 (Переменная result имеет неправильное значение.
# Вы получили неверное количество вхождений символа из переменной search в строке message)

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for search in message:
#     if search == "r":
#         result += 1
# print(result)

# exercise 9

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))
# if first < second:
#     gcd = first
# else:
#     gcd = second
# while first % gcd != 0 or second % gcd!=0:
#     gcd -=1
# print(gcd)

# exercise 10

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     num = int(input("Enter integer (0 for output): "))

#     for sum in num:
#         sum +=1


# exercise 11

# exercise 13
# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""

# for ch in message:
#     offset += message [(message.index(ch))]

# alpha = ' abcdefghijklmnopqrstuvwxyz'
# n = int(input("enter number: "))
# s = input().strip()
# res = ''
# for c in s:
#     res += alpha[(alpha.index(c) + n) % len(alpha)]
# print('Result: "' + res + '"')


# alphabet = " abcdefghijklmnopqrstuvwxyz"
# key = 3
# s = "i am caesar"
# subst = dict(zip(alphabet, alphabet[key:]+alphabet[:key]))
# res = ''.join(map(subst.__getitem__, s))
# print('Result: "' + res + '"')


# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# pos = 0
# for ch in message:
#     if ch.isupper() == True:
#         pos = ord(ch) - ord('A')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("A"))
#         encoded_message = encoded_message + new_char
#     elif ch.islower() == True:
#         pos = ord(ch) - ord('a')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#         encoded_message = encoded_message + new_char
#     else:
#         encoded_message = encoded_message + ch
# print(encoded_message)

# exercise 14

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
# except ZeroDivisionError:
#     print('Divide by zero completed!')
# else:
#     print(f"quantity {chunk}")
# finally:
#     print("By")

# exercise 15

# result = None
# operand = None
# operator = None
# wait_for_number = True

# while True:

# Variant №1

# def sum(a, b):
#     result = a + b
#     return result
# def subtract(a, b):
#     result = a - b
#     return result
# def multiply(a, b):
#     result = a * b
#     return result
# def divide(a, b):
#     result = a / b
#     return result

# def calculate(a, b, operation):
#    result = None

#    if operation == '+':
#        result = sum(a, b)
#    elif operation == '-':
#        result = subtract(a, b)
#    elif operation == '/':
#        result = divide(a, b)
#    elif operation == '*':
#        result = multiply(a, b)
#    else:
#        print('Неизвестная операция')

#    return result

# def run_calculator():
#    # Запрашиваем данные
#    a = float(input('Введите первое число: '))
#    b = float(input('Введите второе число: '))

#    # Запрашиваем тип операции
#    operation = ask_operation()

#    # Производим вычисления
#    result = calculate(a, b, operation)

#    # Выводим результат в консоль
#    print(f'Результат вычислений: {result}')


# def ask_operation():
#    message = '''
# Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter:

# + : Сложение
# - : Вычитание
# / : Деление
# * : Умножение

# Ваш выбор:
#    '''


#    # Создадим список с возможными операциями
#    correct_operations = ['+', '-', '/', '*', '^', '**']
#       # Запрашиваем у пользователя желаемое действие
#    operation = input(message)
#       # Запускаем цикл, если операции нет в списке
#    while operation not in correct_operations:
#        print('Такая операция недоступна. Повторите попытку.')
#        operation = input(message)

#    return operation

# run_calculator()

# Variant 2

# result = None
# operand = None
# operator = None
# wait_for_number = True

# Variant 2
# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     operator = input("Знак (+,-,*,/): ")
#     if operator == '0':
#         break
#     if operator in ('+', '-', '*', '/'):
#         a = float(input('Введите первое число: '))
#         b = float(input('Введите второе число: '))
#         if operator == '+':
#             print("%.2f" % (a+b))
#         elif operator == '-':
#             print("%.2f" % (a-b))
#         elif operator == '*':
#             print("%.2f" % (a*b))
#         elif operator == '/':
#             if y != 0:
#                 print("%.2f" % (a/b))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")
