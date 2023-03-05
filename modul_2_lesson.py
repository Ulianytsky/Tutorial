# a = True
# b = False

# if a and b is True:
#     print ("True")
# else:
#     print("False")

# a = "alisa"

# if type(a) != str():
#     print ("True")
# else:
#     print("False")


# # Conditions
# age = input("Please enter your age: ")
# if int(age) > 18:
#     print("You can enter")
# elif int(age) == 18:
#     print("You are 18 yers old")
# else:
#     print("Sorry...")

# l = ["apple", "orange", "banana"]
# if "orange" in l:
#     print("True")
# else:
#     print("False")


# x = 1
# while x <= 5:
#     print("Hello")
#     x += 1  # x = x + 1 

# message = "Tell something: "
# loop = True

# while loop:
#     command = input(message)
#     if command == "quit":
#         loop = False
#     else:
#         print(command)


# while True:
#     fruits = input()
#     if fruits == "quit":
#         break
#     else:
#         print (f"Yes I love {fruits.title()}")

# num = 0
# while num < 10:
#     num += 1 
#     if num % 2 == 0:
#         continue
#     print(num)

# fruits = ["apple", "orange", "banana"]
# for fruit in fruits:
#     print(fruit)

# list_tuple = [(1, 2), (3,4), (5, 6 )]
# for i, n in list_tuple:
#     print(i, n)

# for letter in "Alisa":
#     print(letter)

# for n in range(1, 10, 2):
#     print(n)

# tasks = ['run', 'sign', 'stop']
# for task in tasks:
#     if task == 'stop':
#         break
#     print(task)


# tasks = ['run', 'sign', 'stop']
# for task in tasks:
#     if task == 'stop':
#         continue
#     print(task)    

# x = int(input("Your number x  "))
# y = int(input("Your number y  "))

# try:
#     res = x / y 
#     print(res)
# except ZeroDivisionError:
#     print("Zero Division")

##################

nums = [1, 4, 8, 3]
k = 0
for n in nums:
    if k < n:
        k = n
print(k)