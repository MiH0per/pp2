import math

print("Input number of sides: ", end = "")
n = int(input())

print("Input the length of a side: ",end = "")

s = float(input())

output = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", round(output))