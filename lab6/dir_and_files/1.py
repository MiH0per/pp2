import os

PATH = "../../"

def list_dirs(path):
    directories = []

    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            directories.append(dir)

    return directories

def lis_files(path):
    files = []

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)

    return files

def list_all(path):
    files_and_dirs = os.listdir(path)
    return files_and_dirs

temp = input("all / dirs / files?")

if temp == "all":
    print(list_all(PATH))
elif temp == "files":
    print(lis_files(PATH))
elif temp == "dirs":
    print(list_dirs(PATH))


