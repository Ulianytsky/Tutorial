# message = 'hello alisa'
# print("Title: ", message.title())
# print("Upper: "message.upper())
# print("Lower:" message.lower())

# first_name = "alisa"
# last_name = "simpson"
# full_name = first_name + " " + last_name
# print("Hello, ", full_name.title())

# email = first_name.lower() + last_name.lower() + "@company.com"
# print(email)


# num1 = input("Enter your number: ")
# num2 = input("Enter your second number: ")
# sum_= float(num1) + float(num2)
# print(f"The sum of {num1} + {num2} is equal {sum_}")

# num = float(input("Enter your number: "))
# num_sqt = num ** 0.5
# print("The sqrt of %0.3f is equal %0.3f"%(num, num_sqt))

# import cmath

# num = 3+4j
# num_sqt = cmath.sqrt(num)
# print("The square root of {0} is {1:.3f}+{2:.4f}".format(num, num_sqt, num_sqt.imag))

#
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))
# p = (a + b + c) / 2
# # print("P = ", p)
# #area
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(f"The perimetr is equal {p}")
# print(f"The area is equal {s}")



# quadratic equation ax**2 + bx + c = 0
import cmath
a = 2
b = 7
c = 8

d = (b ** 2) - (4 * a * c)
result_m = (-b-cmath.sqrt(d)) / (2 * a)
result_p = (-b-cmath.sqrt(d)) / (2 * a)

print(f"Results are {result_m} and {result_p}")


# a = 111
# b = 111

# print(a == b)
