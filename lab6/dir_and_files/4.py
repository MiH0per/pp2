import os
w

filepath = r'dir_and_files/7/input.txt'

def count_lines(path):
    with open(path, 'r') as file:
        lines = 0
        for line in file:
            lines += 1

    return lines

print("Lines:", count_lines(filepath))