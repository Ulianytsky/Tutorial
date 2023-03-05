'''Specsimvol'''

# text = 'Hello\World'
# print(text)
# for i in text:
#     print(i)


'''Metod rjadkiv'''

# text = 'Hello World'
# print(text.capitalize())
# print(text.title())
# print(text.upper())
# print(text.lower())
# print(text.find("l"))


# def find_all(text, substring):
#     start = 0
#     for i in range(len(text)):
#         position = text.find(substring)
#         if position > -1:
#             result.append(position)
#             start_position = position + 1


# print(find_all(text, 'l'))


# def real_len(string):
#     ignore_list = ['\n', '\f', '\r', '\t', '\v']
#     length = 0
#     for i in text:
#         if i not in ignore_list:
#             length += 1
#     return length


# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]


# def find_articles(key, letter_case=False):
#     result = []
#     for article in articles_dict:
#         title = article['title']
#         author = article['author']
#         year = article['year']

#         # змінюємо регістр, якщо необхідно
#         if not letter_case:
#             key = key.lower()
#             title = title.lower()
#             author = author.lower()

#         # перевіряємо, чи зустрічається ключ у назві статті або імені автора
#         if key in title or key in author:
#             # додаємо словник з відформатованими даними до результату
#             result.append({
#                 'title': title.capitalize(),
#                 'author': author.title(),
#                 'year': year
#             })

#     return result


# def sanitize_phone_number(phone):
#     return ''.join(filter(str.isdigit, phone))


# def is_check_name(fullname, first_name):
#     """
#     Перевіряє, чи є рядок first_name префіксом рядка fullname.
#     Приклад використання: is_check_name('Sam Smith', 'sam') => False
#     """
#     # Розділяємо fullname на список слів
#     words = fullname.split()

#     # Перевіряємо, чи починається перше слово на first_name
#     if words[0].lower().startswith(first_name.lower()):
#         return True
#     else:
#         return False


# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):
#     sanitized_phones = [sanitize_phone_number(phone) for phone in list_phones]
#     phone_dict = {"UA": [], "JP": [], "TW": [], "SG": []}

#     for phone in sanitized_phones:
#         if phone.startswith("380"):
#             phone_dict["UA"].append(phone)
#         elif phone.startswith("81"):
#             phone_dict["JP"].append(phone)
#         elif phone.startswith("886"):
#             phone_dict["TW"].append(phone)
#         elif phone.startswith("65"):
#             phone_dict["SG"].append(phone)
#         else:
#             phone_dict["UA"].append(phone)

#     return phone_dict


# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}
# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()


# def translate(name):
#     return name.translate(TRANS)


# print(translate("Дмитрий Коробов"))  # Dmitrij Korobov
# print(translate("Александр Иванович"))  # Aleksandr Ivanovich


# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


# def formatted_grades(students):
#     formatted = []
#     for n, i in enumerate(students.items(), 1):
#         name, grade = i
#         formatted.append("{0:>4}|{1:<10}|{2:^5}|{3:^5}".format(
#             n, name, grade, grades[grade]))
#     return formatted


# def formatted_numbers():
#     table = ['| decimal  |   hex    |  binary  |']
#     for i in range(16):
#         table += [f"|{i:<10}|{i:^10x}|{i:>10b}|"]
#     return table


# import re
# def find_word(text, word):
#     res_dict = {}
#     result = re.search(word, text)
#     if result:
#         res_dict['result'] = True
#         res_dict['first_index'] = result.start()
#         res_dict['last_index'] = result.end()
#     else:
#         res_dict['result'] = False
#         res_dict['first_index'] = None
#         res_dict['last_index'] = None
#     res_dict['search_string'] = word
#     res_dict['string'] = text
#     return res_dict


# import re
# def replace_spam_words(text, spam_words):
#     for word in spam_words:
#         # Создаем регулярное выражение для поиска слова с учетом регистра
#         regex = re.compile(word, re.IGNORECASE)
#         # Заменяем найденное слово на шаблон
#         text = regex.sub('*' * len(word), text)
#     return text




import re
def find_all_emails(text):
    result = re.findall(r'[\w._%+-]+@[\w.-]+\.[a-zA-Z]', text)
    return result


if __name__ == "__main__":
    print(find_all_emails(jhfh@gmail.com))
