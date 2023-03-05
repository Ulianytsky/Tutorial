# def hello(name: str) -> str:
#     return f'Hello {name}'


# name = 'Bill'

# result = hello(name)

# # print(result)
# for n in name:
#     print(hello(n))


"""Lokal and Global"""

name = 'bill'


# def lower_string(text: str) -> str:
#     name = text
#     return name.lower()


# print(lower_string(name))
# print(name)

def global_lower_string(text: str) -> str:
    global name
    return name.lower()


print(lower_string(name))
print(name)
