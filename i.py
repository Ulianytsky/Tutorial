# import os
# import shutil
# import zipfile
# import sys
# from transliterate import translit


# # Функция транслитерации и нормализации имен файлов
# def normalize(name):
#     name = translit(name, 'ru', reversed=True)
#     name = name.lower()
#     name = ''.join(c if c.isalnum() else '_' for c in name)
#     return name


# # Функция обработки папки
# def sort_files(path):
#     # Список расширений файлов, которые мы распознали
#     known_extensions = set()
#     # Список расширений файлов, которые мы не распознали
#     unknown_extensions = set()
#     # Счетчики файлов в каждой категории
#     images_count = 0
#     videos_count = 0
#     documents_count = 0
#     music_count = 0
#     archives_count = 0

#     # Обход файлов в текущей папке
#     for file in os.listdir(path):
#         full_path = os.path.join(path, file)
#         # Если это файл, а не папка
#         if os.path.isfile(full_path):
#             # Получаем расширение файла
#             extension = os.path.splitext(file)[-1][1:].lower()
#             # Если расширение файла известно
#             if extension in ('jpeg', 'png', 'jpg', 'svg'):
#                 # Перемещаем файл в папку images
#                 shutil.move(full_path, os.path.join(path, 'images', normalize(file)))
#                 images_count += 1
#             elif extension in ('avi', 'mp4', 'mov', 'mkv'):
#                 # Перемещаем файл в папку videos
#                 shutil.move(full_path, os.path.join(path, 'videos', normalize(file)))
#                 videos_count += 1
#             elif extension in ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'):
#                 # Перемещаем файл в папку documents
#                 shutil.move(full_path, os.path.join(path, 'documents', normalize(file)))
#                 documents_count += 1
#             elif extension in ('mp






# # Обработка архивов
#     for file in os.listdir(path):
#         full_path = os.path.join(path, file)
#         # Если это файл, а не папка
#         if os.path.isfile(full_path):
#             # Получаем расширение файла
#             extension = os.path.splitext(file)[-1][1:].lower()
#             # Если расширение файла известно
#             if extension in ('zip', 'rar', '7z'):
#                 # Создаем папку с именем архива
#                 archive_folder = os.path.join(path, 'archives', normalize(os.path.splitext(file)[0]))
#                 os.makedirs(archive_folder, exist_ok=True)
#                 # Извлекаем файлы из архива
#                 with zipfile.ZipFile(full_path, 'r') as archive:
#                     archive.extractall(path=archive_folder)
#                 archives_count += 1









# import os
# import shutil
# import zipfile
# import sys
# from transliterate import translit


# # Функция транслитерации и нормализации имен файлов
# def normalize(name):
#     name = translit(name, 'ru', reversed=True)
#     name = name.lower()
#     name = ''.join(c if c.isalnum() else '_' for c in name)
#     return name


# # Функция обработки папки
# def sort_files(path):
#     # Список расширений файлов, которые мы распознали
#     known_extensions = set()
#     # Список расширений файлов, которые мы не распознали
#     unknown_extensions = set()
#     # Счетчики файлов в каждой категории
#     images_count = 0
#     videos_count = 0
#     documents_count = 0
#     music_count = 0
#     archives_count = 0

#     # Обход файлов в текущей папке
#     for file in os.listdir(path):
#         full_path = os.path.join(path, file)
#         # Если это файл, а не папка
#         if os.path.isfile(full_path):
#             # Получаем расширение файла
#             extension = os.path.splitext(file)[-1][1:].lower()
#             # Если расширение файла известно
#             if extension in ('jpeg', 'png', 'jpg', 'svg'):
#                 # Перемещаем файл в папку images
#                 shutil.move(full_path, os.path.join(path, 'images', normalize(file)))
#                 images_count += 1
#             elif extension in ('avi', 'mp4', 'mov', 'mkv'):
#                 # Перемещаем файл в папку videos
#                 shutil.move(full_path, os.path.join(path, 'videos', normalize(file)))
#                 videos_count += 1
#             elif extension in ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'):
#                 # Перемещаем файл в папку documents
#                 shutil.move(full_path, os.path.join(path, 'documents', normalize(file)))
#                 documents_count += 1
#             elif extension in ('mp3', 'ogg', 'wav'):
#                 # Перемещаем файл в папку music
#                 shutil.move(full_path, os.path.join(path, 'music', normalize(file)))
#                 music_count += 1
#             elif extension in ('zip', 'rar'):
#                 # Создаем папку для распакованных файлов
#                 dirname = os.path.join(path, 'archives', normalize(os.path.splitext(file)[0]))
#                 os.makedirs(dirname, exist_ok=True)
#                 # Распаковываем архив
#                 with zipfile.ZipFile(full_path, 'r') as archive:
#                     archive.extractall(dirname)
#                 # Перемещаем архив в папку archives
#                 shutil.move(full_path, os.path.join(path, 'archives', normalize(file)))
#                 archives_count += 1
#             else:
#                 # Расширение файла неизвестно
#                 unknown_extensions.add(extension)

#             # Добавляем расширение в список известных расширений
#             known_extensions.add(extension)

#         # Если это папка, рекурсивно обрабатываем ее
#         elif os.path.isdir(full_path):
#             sort_files(full_path)

#     # Выводим отчет о проделанной работе
#     print('





import os
import shutil
import zipfile
import sys
from transliterate import translit


# Функция транслитерации и нормализации имен файлов
def normalize(name):
    name = translit(name, 'ru', reversed=True)
    name = name.lower()
    name = ''.join(c if c.isalnum() else '_' for c in name)
    return name


# Функция обработки папки
def sort_files(path):
    # Список расширений файлов, которые мы распознали
    known_extensions = set()
    # Список расширений файлов, которые мы не распознали
    unknown_extensions = set()
    # Счетчики файлов в каждой категории
    images_count = 0
    videos_count = 0
    documents_count = 0
    music_count = 0
    archives_count = 0

    # Обход файлов в текущей папке
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        # Если это файл, а не папка
        if os.path.isfile(full_path):
            # Получаем расширение файла
            extension = os.path.splitext(file)[-1][1:].lower()
            # Если расширение файла известно
            if extension in ('jpeg', 'png', 'jpg', 'svg'):
                # Перемещаем файл в папку images
                shutil.move(full_path, os.path.join(path, 'images', normalize(file)))
                images_count += 1
            elif extension in ('avi', 'mp4', 'mov', 'mkv'):
                # Перемещаем файл в папку videos
                shutil.move(full_path, os.path.join(path, 'videos', normalize(file)))
                videos_count += 1
            elif extension in ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'):
                # Перемещаем файл в папку documents
                shutil.move(full_path, os.path.join(path, 'documents', normalize(file)))
                documents_count += 1
            elif extension in ('mp3', 'ogg', 'wav', 'amr'):
                # Перемещаем файл в папку music
                shutil.move(full_path, os.path.join(path, 'music', normalize(file)))
                music_count += 1
            elif extension in ('zip', 'tar', 'gz', 'rar'):
                # Извлекаем архив и перемещаем файлы в соответствующую папку
                with zipfile.ZipFile(full_path, 'r') as archive:
                    archive.extractall(path=os.path.join(path, 'archives'))
                # Удаляем архив
                os.remove(full_path)
                archives_count += 1
            else:
                # Если расширение файла неизвестно, добавляем его в список неизвестных расширений
                unknown_extensions.add(extension)

            # Добавляем расширение файла в список известных расширений
            known_extensions.add(extension)

        # Если это папка, рекурсивно вызываем функцию sort_files() для обработки подпапки
        elif os.path.isdir(full_path):
            sort_files(full_path)

       # Выводим отчет о проделанной работе
    print(f"Обработано {len(known_extensions)} типов файлов: {', '.join(sorted(known_extensions))}")
    if unknown_extensions:
        print(f"Неизвестные расширения: {', '.join(sorted(unknown_extensions))}")
    print(f"Изображений: {images_count}")
    print(f"Видео: {videos_count}")
    print(f"Документов: {documents_count}")
    print(f"Музыка: {music_count}")
    print(f"Архивов: {archives_count}")

