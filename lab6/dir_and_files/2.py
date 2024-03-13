import os 

def check_path(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return

    if os.access(path, os.R_OK):
        print(f"{path} path is readable")
    else: print(f"{path} path is not readable")

    if os.access(path, os.W_OK):
        print(f"{path} path is writable")
    else: print(f"{path} path is not writable")

    if os.access(path, os.X_OK):
        print(f"{path} path is executable")
    else: print(f"{path} path is not execuable")

