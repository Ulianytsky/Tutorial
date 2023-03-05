# import os
# import re
# import transliterate


# def normalize(string):
#     # Транслитерация кириллических символов на латиницу
#     transliterated = transliterate.translit(string, reversed=True)
#     # Замена всех символов, кроме букв латинского алфавита и цифр, на символ '_'
#     replaced = re.sub(r'[^a-zA-Z0-9]+', '_', transliterated)
#     return replaced


# def normalize(string):
#     # Ваша функция normalize из предыдущего ответа


# folder_path = '/Users/vitaliyu/Desktop/Projects/python/Tutorial/folder'

# for name in os.listdir(folder_path):
#     # Полный путь к файлу или папке
#     full_path = os.path.join(folder_path, name)
#     # Нормализуем имя файла или папки
#     normalized_name = normalize(name)
#     # Полный путь к новому имени файла или папки
#     new_full_path = os.path.join(folder_path, normalized_name)
#     # Переименовываем файл или папку
#     os.rename(full_path, new_full_path)
# import os
# import re
# import unicodedata


# def normalize(filename):
#     # переводим в нижний регистр
#     filename = filename.lower()
#     # транслитерация
#     filename = unicodedata.normalize('NFKD', filename).encode(
#         'ascii', 'ignore').decode('ascii')
#     # заменяем символы, кроме букв латинского алфавита и цифр, на символ '_'
#     filename = re.sub(r'[^\w\d]+', '_', filename)
#     # убираем символ '_' в начале и конце имени
#     filename = filename.strip('_')
#     return filename


# def normalize_folder(folder_path):
#     for root, dirs, files in os.walk(folder_path):
#         for dir in dirs:
#             old_path = os.path.join(root, dir)
#             new_dirname = normalize(dir)
#             # получаем новый путь к папке с новым именем
#             new_path = os.path.join(root, new_dirname)
#             if old_path != new_path:
#                 os.rename(old_path, new_path)
#                 print(f'Renamed folder: {old_path} -> {new_path}')
#         for file in files:
#             old_path = os.path.join(root, file)
#             new_filename = normalize(file)
#             # получаем новый путь к файлу с новым именем
#             new_path = os.path.join(root, new_filename)
#             if old_path != new_path:
#                 os.rename(old_path, new_path)
#                 print(f'Renamed file: {old_path} -> {new_path}')


# normalize_folder('/Users/vitaliyu/Desktop/Projects/python/Tutorial/folder')


import os
import re


def normalize(filename):
    # Транслитерация кириллических символов на латиницу
    cyrillic_map = {
        u'а': 'a', u'б': 'b', u'в': 'v', u'г': 'g',
        u'д': 'd', u'е': 'e', u'ё': 'e', u'ж': 'zh',
        u'з': 'z', u'и': 'i', u'й': 'y', u'к': 'k',
        u'л': 'l', u'м': 'm', u'н': 'n', u'о': 'o',
        u'п': 'p', u'р': 'r', u'с': 's', u'т': 't',
        u'у': 'u', u'ф': 'f', u'х': 'kh', u'ц': 'ts',
        u'ч': 'ch', u'ш': 'sh', u'щ': 'shch', u'ъ': '',
        u'ы': 'y', u'ь': '', u'э': 'e', u'ю': 'yu',
        u'я': 'ya'
    }
    translit_filename = ''
    for char in filename:
        if char.lower() in cyrillic_map:
            translit_filename += cyrillic_map[char.lower()]
        else:
            translit_filename += char

    # Замена символов, кроме букв латинского алфавита и цифр, на символ '_'
    normalized_filename = re.sub(r'[^a-zA-Z0-9]', '.', translit_filename)

    return normalized_filename


folder_path = '/Users/vitaliyu/Desktop/Projects/python/Tutorial/folder'

for filename in os.listdir(folder_path):
    normalized_filename = normalize(filename)
    os.rename(os.path.join(folder_path, filename),
              os.path.join(folder_path, normalized_filename))
