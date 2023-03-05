import os
import re


def normalize(filename):
    # Transliteration of Cyrillic characters into Latin
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

    # Replacing characters, except for letters of the Latin alphabet and numbers, with the symbol '_'
    normalized_filename = re.sub(r'[^a-zA-Z0-9]', '.', translit_filename)

    return normalized_filename


main_path = '/Users/vitaliyu/Desktop/Projects/python/Tutorial/folder'

for filename in os.listdir(main_path):
    normalized_filename = normalize(filename)
    os.rename(os.path.join(main_path, filename),
              os.path.join(main_path, normalized_filename))


main_path = 'folder'


# key names for folder names
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


# creates folders from dictionary keys
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}/{folder}'):
            os.mkdir(f'{folder_path}/{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('/')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(
                    f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(
                    file_path, f'{main_path}/{ext_list[dict_key_int][0]}/{file_name}')


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('/')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)
