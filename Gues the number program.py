# This is a guess the numbe game
import random

print("Hello, what is your name?")
name = input()
print("Well " + name + " I am thinking of a number between 1 and 20")
secretNumber = random.randint(1,20)
print(secretNumber)
for guessTaken in range(1, 7):
    print("take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
            break # THis condition is for the correct answer
if guess == secretNumber:
    print("you guessed it in " + str(guessTaken) + " Time")
else:
    print("Nope, the number I was thinkig of was" + str(secretNumber))
