import math, time

num = int(input())
ms = int(input())

time.sleep(ms/1000)

root = math.sqrt(num)

print(f"Square root of {num} after {ms} milliseconds is {root}")

