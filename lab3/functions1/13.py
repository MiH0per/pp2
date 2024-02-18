from random import randint

def GTN():
    print("Hello what is your name?")
    name = str(input())
    print("Well, " + name + ", I am thinking of a number between 1 and 20. \nTake a guess.")

    number = randint(1, 20)
    count = 1

    while(True):
        g = int(input())
        if g < number:
            print("Your guess is too low. \nTake a guess.")
            count += 1
        elif g > number:
            print("Your guess is too high. \nTake a guess.")
            count += 1
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            return
        
GTN()