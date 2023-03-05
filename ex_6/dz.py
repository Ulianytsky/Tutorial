import os

# вывести текущую директорию
# print("Текущая деректория:", os.getcwd())


'''Создание и удаление каталогов'''
# создать пустой каталог (папку)
# os.mkdir("folder")
# os.mkdir('folder/new')
# удалить папку
# os.chdir('folder/new')

'''Для удаления каталогов рекурсивно необходимо использовать os.removedirs():'''
# удалить вложенные папки
# os.removedirs("folder/new") #Это удалит только пустые каталоги.

# # изменение текущего каталога на 'folder'
# os.chdir("folder")


# # вернуться в предыдущую директорию
# os.chdir("..")

# # сделать несколько вложенных папок
# os.makedirs("nested1/nested2/nested3")

'''функция обработки папок рекурсивно вызывать сама себя, когда ей встречаются вложенные папки.'''
# def process_folder(path):
#     # Обработка текущей папки
#     for filename in os.listdir(path):
#         full_path = os.path.join(path, filename)
#         if os.path.isfile(full_path):
#             # Обработка файла
#             process_file(full_path)
#         elif os.path.isdir(full_path):
#             # Рекурсивный вызов функции для обработки вложенной папки
#             process_folder(full_path)

'''Cоздать новый текстовый файл'''
# # создать новый текстовый файл
# fh = open('test.txt', "w")
# data = fh.write()
# fh.close()

'''Удаление файлов'''
# удалить файл из папки
# os.chdir("folder")
# os.replace("renamed-text.txt",
#            "new/renamed-text.txt")
# os.remove("new/renamed-text.txt")
# print("Текущая деректория:", os.getcwd())

'''Переименовать файлы'''
# # переименовать text.txt на renamed-text.txt
# os.rename("test.txt", "renamed-text.txt")


'''Перемещение файлов'''
# # заменить (переместить) этот файл в другой каталог
# # Стоит обратить внимание, что это перезапишет путь, поэтому если в папке folder уже есть файл с таким же именем (renamed-text.txt), он будет перезаписан.
# os.replace("renamed-text.txt",
#            "/new/renamed-text.txt")


'''Список файлов и директорий'''


# распечатать все файлы и папки в текущем каталоге

# os.chdir("..")  # вернуться в предыдущую директорию
# print("Текущая деректория:", os.getcwd())
# print("Все папки и файлы:", os.listdir())

# os.chdir("ex_6")
# print("Текущая деректория:", os.getcwd())
# print("Все папки и файлы:", os.listdir())


# # распечатать все файлы и папки рекурсивно
# for dirpath, dirnames, filenames in os.walk("."):
#     # перебрать каталоги
#     for dirname in dirnames:
#         print("Каталог:", os.path.join(dirpath, dirname))
#     # перебрать файлы
#     for filename in filenames:
#         print("Файл:", os.path.join(dirpath, filename))

'''Сортируем файлы с помощью Python'''

# main_path = 'folder'  # Создадим переменную для пути папки
# os.mkdir(main_path + '/temp')  # Создадим папку в папке

# Создаем много папок
'''Напишем функцию для создания папок из списка названий. 
Для каждого названия проверяем существование папки с помощью метода os.path.exists().'''


# def create_folders_from_list(folder_path, folder_names):
#     for folder in folder_names:
#         if not os.path.exists(f'{folder_path}\\{folder}'):
#             os.mkdir(f'{folder_path}\\{folder}')


''' Cоздаем словарь extensions. Ключи - названия папок. Значения - расширения файлов для каждой отдельной папки.'''
# key names will be folder names!
extensions = {
    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
              'tiff'],

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v',
              'h264', 'flv', 'rm', 'swf', 'vob', 'gif'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],

    'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

    'documents': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt', 'xlsx', 'xls', 'xlsm',
                  'ods', 'pptx', 'ppt', 'pps', 'key', 'odp'],

}

'''Передаем в функцию create_folders_from_list() новоиспеченный словарь. Папки создадутся из названий ключей.'''


def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


'''Получаем пути подпапок и файлов.
Пишем функцию для получения путей подпапок. Для каждого объекта в методе os.scandir() проверяем, является ли он каталогом.'''


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


'''Теперь получим пути всех файлов в папке, скопируем функцию get_subfolder_paths() и добавим в условие генератора not.'''


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


'''Получение имен файлов'''


# def get_file_names(folder_path) -> list:
#     file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
#     file_names = [f.split('\\')[-1] for f in file_paths]

#     return file_names

'''Сортируем файлы
Приступаем к функции сортировки. Получаем пути файлов в переменную file_paths. 
Создаем переменную ext_list со списком метода словаря extensions.items(). 
Обращение к списку по индексу возвращает нам пару ключ-значение в виде списка, первый элемент 
которого - это ключ или название папки в нашем проекте, а второй элемент - это значение, то есть 
асширения файлов для этой папки.'''


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())


# Теперь создадим цикл для каждого пути файла в списке. Вытащим отдельно расширение и имя файла.
    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]


# Создадим еще один цикл внутри. Для каждого ключа в словаре мы проверяем, есть ли
# расширение файла в списке расширений. Если есть, то перемещаем файл.

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(
                    f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(
                    file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


'''Удаляем пустые папки
Остался последний штрих - удаление пустых папок. Все просто. Создаем функцию. 
олучаем пути подпапок. Проверяем, какой список возвращает метод os.listdir("folder_path") для каждой подпапки.
Если возвращается пустой список, значит удаляем папку с помощью os.rmdir("folder_path")'''


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)
