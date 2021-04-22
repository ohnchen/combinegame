#!/usr/bin/env python3 
import random 

# Header
print("Press enter to turn over the next card.")
print("Press r to put in your solution.")
print("Press e to exit the game.")

suspects = ["a", "b", "c", "d", "e", "f", "g"]
numberofsus = 3

def getsolution():
    return random.sample(suspects, numberofsus)

def turnovercard(s):
    tipp = random.sample(suspects, numberofsus)
    combo = list(zip(s, tipp))
    counter = 0

    for i in range(0, 3):
        if combo[i][0] == combo[i][1]:
            counter += 1
        else:
            pass
    print(" ".join(tipp), counter, end=" ")


solution = getsolution()

trys = 0
while True:
    b = input()
    if b == "":
        turnovercard(solution)
        trys += 1
    elif b == "e":
        break
    else:
        guess = input("Enter your solution!")
        if guess == " ".join(solution):
            input(f"Nice! It only took {trys} trys to get it right!")
            break
        else:
            input("Unfortunately that was not right...")
            break


