buffer = ""

input_file = r'C:\Users\maksi\OneDrive\Рабочий стол\Миша\PP2\lab6\dir_and_files\7\input.txt'
output_file = r'C:\Users\maksi\OneDrive\Рабочий стол\Миша\PP2\lab6\dir_and_files\7\output.txt'

def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src:
        with open(destination_file, 'w') as dest:
            dest.write(src.read())
    




copy_file(input_file, output_file)