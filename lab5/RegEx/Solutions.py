import re

# with open('row.txt', 'r', encoding='utf-8') as file:

#     data = file.read()

# #1  Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
# def first(text):
#     x = re.findall(r"ab*", text)
#     return x


# #2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

# def second(text):
#     y = re.findall(r"ab{2,3}", text)
#     return y


# #3  Write a Python program to find sequences of lowercase letters joined with a underscore.

# def third(text):
#     z = re.findall(r"[a-z]_[a-z]", text)
#     return z



#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# def fourth(text):
#     a = re.findall(r"[A-Z][a-z]", text)
#     return a

# print(fourth("Hello world!"))

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# def fifth(text):
#     b = re.fullmatch(r"a.*b", text)
#     return b

# print(fifth("asdsfsbb ggff"))


# #6 Write a Pyhon program to replace all occurrences of space, comma, or dot with a colon.

# def sixth(text):
#     change = r'[ ,.]'
#     c = re.sub(change, ":", text)
#     return c



# #7 Write a python program to convert snake case string to camel case string.

# strings = "turn_into_camel"
# def seventh(text):

#     return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text) #в group() индексирование начинается не с 0 а с 1

# print(seventh(strings))


# #8 Write a Python program to split a string at uppercase letters.

# def eigths(text):
#      return re.findall(r'[A-Z][^A-Z]*',text)

# print(eigths("HelloWorld"))


# #9 Write a Python program to insert spaces between words starting with capital letters.

def ninth(text):        
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)          #\1 \2 индексы групп в скобках ([a-z]) первая группа | ([A-Z]) вторая группа

#print(ninth("testingTheMessagesTothisExercise"))

# #10 Write a Python program to convert a given camel case string to snake case.


def tenth(text):
     return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower() 


print(tenth("testingTheMessagesTothisExercise"))
