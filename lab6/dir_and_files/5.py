import os

PATH = '/../..'
list = [1,2,3,4,5,6,7,8,9]

def line_in_file(path, list):
    with open(path, 'w') as file:
        for item in list:
            file.write(str(item) + "\n")

    file.close()

    print("list was written to the file", PATH)