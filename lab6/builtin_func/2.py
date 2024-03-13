import math

test_in = "Text Text TEST"
upper = sum(1 for ch in test_in if ch.isupper())
lower = sum(1 for ch in test_in if ch.islower())

print(f"Upper: {upper}\nLower: {lower}")