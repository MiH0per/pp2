#Read in a Fahrenheit temperature. 
#Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def FahrToCel(F):
    C = (5 / 9) * (F - 32)
    return C

y = int(input())

print(FahrToCel(y))