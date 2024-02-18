def IsPalindrome(input):
    if input == input[::-1]:
        return True
    return False

print(IsPalindrome("msdm"))