#You are given list of numbers separated by spaces.
#Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def filter_prime(list):
    for num in list:
        num = int(num)
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if (is_prime):
            print(num)
listik = [1,5,6,7,8,2345,86]
filter_prime(list)  