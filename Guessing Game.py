# Guessing Game 

import random

number = random.randint(1,20)
guess = int(input("I'm thinking of a number between 1 to 20. What is it?"))

while guess != number:
    if guess < number:
        print("Your number is to low...")
    else:
        print("Your nuber is to high...")
    guess = int(input("Please try again..."))
print("Congratulations! Correct answer!")
