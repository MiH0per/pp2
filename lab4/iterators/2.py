def EvenNumbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input(""))

even_numbers = list(EvenNumbers(n))

print(even_numbers)