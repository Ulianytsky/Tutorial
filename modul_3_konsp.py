# def fun(a, b=5, c=10):
#     print('a равно', a, ', b равно', b, ', а c равно', c)


# fun(3, 7)          # a равно 3, b равно 7, а c равно 10
# fun(25, c=24)      # a равно 25, b равно 5, а c равно 24
# fun(c=50, a=100)   # a равно 100, b равно 5, а c равно 50

# def discount_price(price=100, discount=0.9):

#     def apply_discount():
#         nonlocal price
#         price = price - price * discount
#         print(price)

#     apply_discount()
#     return price


# discount_price()

# def get_fullname(name,  full_name, middle_name=""):

#     if middle_name:
#         return f" {name} {middle_name} {full_name} "
#     else:
#         return f" {name} {full_name}"


def get_fullname(first_name, middle_name, last_name):

    if middle_name:
        return (f"{first_name} {middle_name} {last_name}")
    else:
        return (f"{first_name} {last_name}")


print(get_fullname)
