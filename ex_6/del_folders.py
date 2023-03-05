import os
# os.chdir('folder')
# print("Текущая деректория:", os.getcwd())


def remove_empty_folders(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir in dirs:
            path = os.path.join(root, dir)
            if not os.listdir(path):
                os.rmdir(path)


remove_empty_folders('/Users/vitaliyu/Desktop/Projects/python/Tutorial/folder')
