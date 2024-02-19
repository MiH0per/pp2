def squares(a,b):
    for i in range(a,b):
        yield i**2

m = int(input())
n = int(input())

nums = squares(m,n)

for i in nums:
    print(i)


for i in range(m,n):
    print(i*i, end=" ")



