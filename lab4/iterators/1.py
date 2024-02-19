#Create a generator that generates the squares of numbers up to some number N.
def squares(N):
    for i in range(1, N+1):
        yield i*i


N = int(input())
nums = squares(N)
for square in nums:
    print(square)
