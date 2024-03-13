import os


def find_path(path):
    if not os.path.exists(path):
        print(f"Path {path} does not exist")
        return
    else: print(f"Path exists")

    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print(filename)
    print(directory)

    
